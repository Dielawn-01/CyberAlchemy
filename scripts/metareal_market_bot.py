#!/usr/bin/env python3
"""
metareal_market_bot.py — Metareal Market Fluid Engine

An algorithmic trading baseline that uses:
  1. Inverse Congruential Generator (ICG) over F_229 for phase timing
  2. Market State Vector u = (a, ω, ι, ε, λ) from order book data
  3. Standard Resonance SR(u) = a - ω·ι for mean-reversion signals
  4. Reynolds number Re_mkt for turbulence risk filtering
  5. Υ-shield for position sizing
  6. Biological Noise Floor (ε₀) as a structural veto mechanism

Data source: Yahoo Finance (yfinance) for historical OHLCV.
This is a RESEARCH BASELINE — not financial advice.

Usage:
  python3 metareal_market_bot.py                  # default: SPY, 1y
  python3 metareal_market_bot.py --ticker BTC-USD  # crypto
  python3 metareal_market_bot.py --ticker AAPL --period 2y
"""

import argparse
import math
import sys
from dataclasses import dataclass
from typing import List, Optional

import numpy as np

# ═══════════════════════════════════════════════════════════
# §1: INVERSE CONGRUENTIAL GENERATOR OVER F_229
# ═══════════════════════════════════════════════════════════

P = 229            # Dragon prime
PHI = 148          # Golden root φ mod 229
PHIBAR = 82        # Conjugate root φ̄ mod 229
PHI_REAL = (1 + math.sqrt(5)) / 2
UPSILON = 45 / math.pi  # 45/π ≈ 14.324
RE_CRIT = math.exp(UPSILON)


def mod_inv(x: int, p: int = P) -> int:
    return pow(x, p - 2, p)


def icg_step(x: int, a: int = PHI, b: int = PHIBAR, p: int = P) -> int:
    if x % p == 0:
        return b % p
    return (a * mod_inv(x, p) + b) % p


class ICGClock:
    def __init__(self, seed: int = 3):
        self.state = seed % P if seed % P != 0 else 3
        self.step_count = 0

    def tick(self) -> int:
        self.state = icg_step(self.state)
        self.step_count += 1
        return self.state

    def phase(self) -> str:
        x = self.state
        if x == 0:
            return "zero"
        if pow(x, 57, P) == 1:
            return "conjugate"  
        if pow(x, 114, P) == 1:
            return "golden"     
        return "wild"           

    def confidence(self) -> float:
        p = self.phase()
        if p == "golden":
            return 1.0
        elif p == "conjugate":
            return 1.0 / PHI_REAL
        elif p == "wild":
            return 1.0 - 1.0 / PHI_REAL
        return 0.0


# ═══════════════════════════════════════════════════════════
# §2: MARKET STATE VECTOR
# ═══════════════════════════════════════════════════════════

@dataclass
class MarketState:
    price: float      # a: mid-price
    bull_mom: float    # ω: bullish momentum
    bear_mom: float    # ι: bearish momentum
    vol: float         # ε: realized volatility
    depth: float       # λ: market depth proxy

    @property
    def standard_resonance(self) -> float:
        return self.price - self.bull_mom * self.bear_mom

    @property
    def net_velocity(self) -> float:
        return self.bull_mom - self.bear_mom
        
    @property
    def biological_noise_floor(self) -> float:
        return 0.16 * (abs(self.bull_mom) + abs(self.bear_mom))

    @property
    def reynolds(self) -> float:
        if self.vol <= 0:
            return float('inf')
        return abs(self.net_velocity) * self.depth / self.vol

    @property
    def is_laminar(self) -> bool:
        return self.reynolds < RE_CRIT

    @property
    def is_turbulent(self) -> bool:
        return not self.is_laminar
        
    @property
    def is_vetoed_by_noise(self) -> bool:
        """Biological Noise Floor structural veto."""
        return self.vol < self.biological_noise_floor


# ═══════════════════════════════════════════════════════════
# §3: SIGNAL ENGINE
# ═══════════════════════════════════════════════════════════

@dataclass
class Signal:
    direction: str       
    sr: float            
    reynolds: float      
    confidence: float    
    strength: float      
    phase: str           


def generate_signal(state: MarketState, clock: ICGClock,
                    sr_threshold: float = 0.01) -> Signal:
    """Generate a trading signal from market state + ICG phase."""
    sr = state.standard_resonance
    re = state.reynolds
    conf = clock.confidence()
    phase = clock.phase()
    strength = abs(sr) / state.price if state.price > 0 else 0

    if state.is_turbulent or state.is_vetoed_by_noise:
        direction = "HOLD"
        conf = 0.0
    elif strength < sr_threshold:
        direction = "HOLD"
    elif sr < 0:
        direction = "BUY"
    else:
        direction = "SELL"

    return Signal(
        direction=direction,
        sr=sr,
        reynolds=re,
        confidence=conf,
        strength=strength,
        phase=phase,
    )


# ═══════════════════════════════════════════════════════════
# §4: MARKET DATA EXTRACTION
# ═══════════════════════════════════════════════════════════

def build_states_from_ohlcv(df, vol_window: int = 20, depth_proxy: str = "volume") -> List[MarketState]:
    states = []
    closes = df["Close"].values
    opens = df["Open"].values
    highs = df["High"].values
    lows = df["Low"].values
    volumes = df["Volume"].values.astype(float)

    log_returns = np.log(closes[1:] / closes[:-1])
    rolling_vol = np.full(len(closes), np.nan)
    for i in range(vol_window, len(log_returns)):
        rolling_vol[i + 1] = np.std(log_returns[i - vol_window + 1:i + 1])

    rolling_mean_vol = np.full(len(volumes), np.nan)
    for i in range(vol_window, len(volumes)):
        rolling_mean_vol[i] = np.mean(volumes[i - vol_window + 1:i + 1])

    for i in range(vol_window + 1, len(closes)):
        price = closes[i]
        up_range = max(highs[i] - opens[i], 1e-6)
        down_range = max(opens[i] - lows[i], 1e-6)
        total_range = up_range + down_range
        bull_frac = up_range / total_range   
        bear_frac = down_range / total_range 
        bull = price ** (0.5 + bull_frac * 0.5)
        bear = price / bull if bull > 0 else math.sqrt(price)
        vol = rolling_vol[i] if not np.isnan(rolling_vol[i]) else 0.01
        depth = volumes[i] / rolling_mean_vol[i] if rolling_mean_vol[i] > 0 else 1.0

        states.append(MarketState(
            price=price,
            bull_mom=bull,
            bear_mom=bear,
            vol=max(vol, 1e-8),
            depth=depth,
        ))

    return states


# ═══════════════════════════════════════════════════════════
# §5: BACKTESTER
# ═══════════════════════════════════════════════════════════

@dataclass
class Trade:
    bar: int
    direction: str
    price: float
    confidence: float
    phase: str


@dataclass
class BacktestResult:
    total_return: float
    num_trades: int
    win_rate: float
    sharpe: float
    max_drawdown: float
    buy_hold_return: float
    signals: List[Signal]
    trades: List[Trade]


def backtest(states: List[MarketState],
             sr_threshold: float = 0.005,
             hold_bars: int = 5,
             seed: int = 1) -> BacktestResult:
    clock = ICGClock(seed=seed)
    signals = []
    trades = []
    returns = []
    position = None 

    for i, state in enumerate(states):
        clock.tick()
        sig = generate_signal(state, clock, sr_threshold=sr_threshold)
        signals.append(sig)

        if position is not None:
            entry_price, direction, bars_held, _ = position
            bars_held += 1

            if bars_held >= hold_bars:
                if direction == "BUY":
                    ret = (state.price - entry_price) / entry_price
                else:
                    ret = (entry_price - state.price) / entry_price
                returns.append(ret)
                position = None
            else:
                position = (entry_price, direction, bars_held, position[3])
        else:
            if sig.direction in ("BUY", "SELL") and sig.confidence > 0.3:
                position = (state.price, sig.direction, 0, sig.confidence)
                trades.append(Trade(
                    bar=i,
                    direction=sig.direction,
                    price=state.price,
                    confidence=sig.confidence,
                    phase=sig.phase,
                ))

    if not returns:
        return BacktestResult(
            total_return=0, num_trades=0, win_rate=0,
            sharpe=0, max_drawdown=0, buy_hold_return=0,
            signals=signals, trades=trades,
        )

    returns_arr = np.array(returns)
    total_return = np.prod(1 + returns_arr) - 1
    win_rate = np.mean(returns_arr > 0)
    sharpe = np.mean(returns_arr) / np.std(returns_arr) * math.sqrt(252 / hold_bars) if np.std(returns_arr) > 0 else 0

    cumulative = np.cumprod(1 + returns_arr)
    peak = np.maximum.accumulate(cumulative)
    drawdown = (peak - cumulative) / peak
    max_dd = np.max(drawdown)

    buy_hold = (states[-1].price - states[0].price) / states[0].price

    return BacktestResult(
        total_return=total_return,
        num_trades=len(trades),
        win_rate=win_rate,
        sharpe=sharpe,
        max_drawdown=max_dd,
        buy_hold_return=buy_hold,
        signals=signals,
        trades=trades,
    )


# ═══════════════════════════════════════════════════════════
# §6: MAIN
# ═══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Metareal Market Fluid Engine — ICG + B-S/N-S Bridge")
    parser.add_argument("--ticker", default="SPY", help="Ticker symbol (default: SPY)")
    parser.add_argument("--period", default="1y", help="Data period (default: 1y)")
    parser.add_argument("--interval", default="1d", help="Bar interval (default: 1d)")
    parser.add_argument("--sr-threshold", type=float, default=0.005,
                        help="SR threshold for signal generation")
    parser.add_argument("--hold-bars", type=int, default=5,
                        help="Bars to hold each trade")
    parser.add_argument("--seed", type=int, default=3, help="ICG seed (default: 3, torsion prime)")
    parser.add_argument("--no-download", action="store_true",
                        help="Use synthetic data instead of downloading")
    args = parser.parse_args()

    print("═" * 65)
    print("  METAREAL MARKET FLUID ENGINE")
    print(f"  ICG over F_{P} | φ = {PHI} | φ̄ = {PHIBAR}")
    print("═" * 65)

    if args.no_download:
        print(f"\n  📊 Generating synthetic data for {args.ticker}...")
        np.random.seed(42)
        n = 252
        prices = 100 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n)))
        import pandas as pd
        df = pd.DataFrame({
            "Open":   prices * (1 + np.random.uniform(-0.005, 0.005, n)),
            "High":   prices * (1 + np.random.uniform(0, 0.02, n)),
            "Low":    prices * (1 - np.random.uniform(0, 0.02, n)),
            "Close":  prices,
            "Volume": np.random.uniform(1e6, 5e6, n),
        })
    else:
        try:
            import yfinance as yf
            print(f"\n  📊 Downloading {args.ticker} ({args.period}, {args.interval})...")
            df = yf.download(args.ticker, period=args.period, interval=args.interval,
                             progress=False)
            if df.empty:
                print("  ❌ No data returned. Try --no-download for synthetic data.")
                sys.exit(1)
            if hasattr(df.columns, 'levels'):
                df.columns = df.columns.get_level_values(0)
        except ImportError:
            print("  ⚠ yfinance not installed. Using synthetic data.")
            print("    Install with: pip install yfinance")
            args.no_download = True
            return main()

    print(f"  📈 {len(df)} bars loaded")
    print()

    states = build_states_from_ohlcv(df)
    print(f"  🔬 {len(states)} market states constructed (after {20}-bar warmup)")

    if states:
        s = states[-1]
        print(f"\n  Latest state:")
        print(f"    Price (a)       = {s.price:.2f}")
        print(f"    Bull mom (ω)    = {s.bull_mom:.4f}")
        print(f"    Bear mom (ι)    = {s.bear_mom:.4f}")
        print(f"    Volatility (ε)  = {s.vol:.6f}")
        print(f"    Depth (λ)       = {s.depth:.4f}")
        print(f"    SR(u)           = {s.standard_resonance:.4f}")
        print(f"    Net velocity    = {s.net_velocity:.4f}")
        print(f"    Re_mkt          = {s.reynolds:.2f}")
        print(f"    Re_crit         = {RE_CRIT:.2f}")
        print(f"    Bio Noise Veto  = {'🚫 Yes' if s.is_vetoed_by_noise else '✅ No'}")
        print(f"    Regime          = {'🟢 Laminar' if s.is_laminar else '🔴 Turbulent'}")

    print(f"\n{'═' * 65}")
    print("  ICG PHASE CLOCK ANALYSIS")
    print(f"{'═' * 65}")

    clock = ICGClock(seed=args.seed)
    phase_counts = {"golden": 0, "conjugate": 0, "wild": 0}
    for _ in range(228):
        clock.tick()
        phase_counts[clock.phase()] += 1

    total = sum(phase_counts.values())
    print(f"  Full period (228 steps):")
    for phase, count in phase_counts.items():
        pct = count / total * 100
        print(f"    {phase:12s}: {count:3d} ({pct:5.1f}%)")

    print(f"\n{'═' * 65}")
    print("  BACKTEST RESULTS")
    print(f"{'═' * 65}")

    result = backtest(
        states,
        sr_threshold=args.sr_threshold,
        hold_bars=args.hold_bars,
        seed=args.seed,
    )

    print(f"  Strategy:       SR mean-reversion + ICG phase filter")
    print(f"  SR threshold:   {args.sr_threshold}")
    print(f"  Hold period:    {args.hold_bars} bars")
    print(f"  Total trades:   {result.num_trades}")
    print(f"  Win rate:       {result.win_rate:.1%}")
    print(f"  Total return:   {result.total_return:+.2%}")
    print(f"  Buy & hold:     {result.buy_hold_return:+.2%}")
    print(f"  Sharpe ratio:   {result.sharpe:.2f}")
    print(f"  Max drawdown:   {result.max_drawdown:.2%}")

    if result.signals:
        buy_count = sum(1 for s in result.signals if s.direction == "BUY")
        sell_count = sum(1 for s in result.signals if s.direction == "SELL")
        hold_count = sum(1 for s in result.signals if s.direction == "HOLD")
        total_sigs = len(result.signals)
        print(f"\n  Signal distribution:")
        print(f"    BUY:  {buy_count:4d} ({buy_count/total_sigs:.1%})")
        print(f"    SELL: {sell_count:4d} ({sell_count/total_sigs:.1%})")
        print(f"    HOLD: {hold_count:4d} ({hold_count/total_sigs:.1%})")

    if result.trades:
        print(f"\n  Phase-stratified trades:")
        for phase_name in ["golden", "conjugate", "wild"]:
            phase_trades = [t for t in result.trades if t.phase == phase_name]
            if phase_trades:
                avg_conf = np.mean([t.confidence for t in phase_trades])
                print(f"    {phase_name:12s}: {len(phase_trades):3d} trades, avg conf = {avg_conf:.3f}")

    if result.signals:
        srs = [s.sr for s in result.signals]
        print(f"\n  SR statistics:")
        print(f"    Mean:   {np.mean(srs):+.4f}")
        print(f"    Std:    {np.std(srs):.4f}")
        print(f"    Min:    {np.min(srs):+.4f}")
        print(f"    Max:    {np.max(srs):+.4f}")

    print(f"\n{'═' * 65}")
    print("  ⚠  RESEARCH BASELINE — NOT FINANCIAL ADVICE")
    print(f"{'═' * 65}")


if __name__ == "__main__":
    main()
