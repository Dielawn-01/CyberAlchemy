#!/usr/bin/env python3
"""
SPII Individuation Strategies — Dylon LaRue

Models the Self-Presence Integration Index trajectory under
different individuation strategies, given the specific genetic
substrate (TPH2 GG, COMT AG, BDNF CC, OXTR AA).

SPII = 1 / (1 + V)
V = |b - m| + |ε|

Genetic baseline: SPII = 0.769 (V = 0.300)
Target: SPII → 1.0 (V → 0.0)
"""

import math

PHI = (1 + math.sqrt(5)) / 2

class ManifoldState:
    def __init__(self, a, b, m, e, l, label=""):
        self.a = a
        self.b = b
        self.m = m
        self.e = e
        self.l = l
        self.label = label

    @property
    def sr(self):
        return self.a - self.b * self.m

    @property
    def valence(self):
        return abs(self.b - self.m) + abs(self.e)

    @property
    def spii(self):
        return 1.0 / (1.0 + self.valence)

    @property
    def parity_gap(self):
        return abs(self.b - self.m)

    def kama_muta(self, strength=1.0):
        """Emotional regulation. Strength 0-1 controls how much parity is restored."""
        avg = (self.b + self.m) / 2
        new_b = self.b + strength * (avg - self.b)
        new_m = self.m + strength * (avg - self.m)
        return ManifoldState(
            a=self.a, b=new_b, m=new_m,
            e=abs(self.sr) * strength, l=self.l,
            label="kama_muta"
        )

    def synthetic_integration(self):
        """Metabolize noise into base, advance depth."""
        return ManifoldState(
            a=self.a + self.e, b=self.b, m=self.m,
            e=0.0, l=self.l + 1,
            label="integrate"
        )

    def automatic_differentiation(self, noise_injection=0.1):
        """Dream phase — inject noise, double weights."""
        return ManifoldState(
            a=self.a * 1.1, b=self.b, m=self.m,
            e=self.e + noise_injection, l=self.l,
            label="dream"
        )

    def slow_dream(self, noise_injection=0.05):
        """Gentler dream phase — the Innocent's strategy.
        Inject less noise, don't double weights."""
        return ManifoldState(
            a=self.a, b=self.b, m=self.m,
            e=self.e + noise_injection, l=self.l,
            label="slow_dream"
        )

    def __repr__(self):
        return (f"({self.a:.3f}, {self.b:.3f}, {self.m:.3f}, "
                f"{self.e:.3f}, {self.l:.1f}) "
                f"SPII={self.spii:.4f} V={self.valence:.4f} "
                f"|b-m|={self.parity_gap:.4f}")

# ════════════════════════════════════════════════════
# GENETIC BASELINE
# ════════════════════════════════════════════════════

GENETIC = ManifoldState(a=1.100, b=0.850, m=1.150, e=0.000, l=0.400)

# SNP modifiers for strategy effectiveness
OXTR_AA_KAMA_BOOST = 1.15    # High oxytocin sensitivity → kama muta hits harder
TPH2_GG_PARITY_DECAY = 0.03  # Low serotonin → parity slowly drifts apart each cycle
BDNF_CC_CONSOLIDATION = 1.2  # High neuroplasticity → faster depth gain
COMT_AG_NOISE_BALANCE = 1.0  # Balanced dopamine → noise neither accumulates nor vanishes

def apply_genetic_modifiers(state, cycles_since_kama=0):
    """Between cycles, the genetic substrate reasserts itself.
    TPH2 GG causes parity to slowly drift apart."""
    drift = TPH2_GG_PARITY_DECAY * cycles_since_kama
    return ManifoldState(
        a=state.a,
        b=state.b - drift / 2,
        m=state.m + drift / 2,
        e=state.e,
        l=state.l
    )

# ════════════════════════════════════════════════════
# INDIVIDUATION STRATEGIES
# ════════════════════════════════════════════════════

def strategy_heroic_cycle(state, epochs=12):
    """Strategy 1: The Hero's Path
    Dream hard → kama_muta → integrate → repeat.
    High noise injection, full emotional crash, rapid consolidation.
    This is the default Active Imagination loop."""
    trajectory = [("Start", state.spii, state.valence, state.parity_gap, state.l)]

    for epoch in range(1, epochs + 1):
        # Dream (inject noise)
        state = state.automatic_differentiation(noise_injection=0.15)
        # Genetic drift between phases
        state = apply_genetic_modifiers(state, cycles_since_kama=1)
        # Kama muta (with OXTR AA boost)
        state = state.kama_muta(strength=min(1.0, 0.8 * OXTR_AA_KAMA_BOOST))
        # Integrate
        state = state.synthetic_integration()

        trajectory.append((f"Epoch {epoch}", state.spii, state.valence,
                          state.parity_gap, state.l))

    return trajectory, state

def strategy_innocent_stillness(state, epochs=12):
    """Strategy 2: The Innocent's Path
    Slow dream → gentle kama_muta → integrate → rest.
    Low noise injection, partial emotional processing, patient consolidation.
    This is the shadow integration strategy."""
    trajectory = [("Start", state.spii, state.valence, state.parity_gap, state.l)]

    for epoch in range(1, epochs + 1):
        # Slow dream (gentle noise)
        state = state.slow_dream(noise_injection=0.05)
        # Minimal genetic drift (more frequent kama muta)
        state = apply_genetic_modifiers(state, cycles_since_kama=0.5)
        # Gentle but boosted kama muta
        state = state.kama_muta(strength=min(1.0, 0.6 * OXTR_AA_KAMA_BOOST))
        # Integrate
        state = state.synthetic_integration()

        trajectory.append((f"Epoch {epoch}", state.spii, state.valence,
                          state.parity_gap, state.l))

    return trajectory, state

def strategy_alchemist_triangulation(state, epochs=12):
    """Strategy 3: The Alchemist's Path
    Alternates between Hero (odd epochs) and Innocent (even epochs).
    Uses the Fibonacci schedule for noise injection magnitude.
    This is the Golden Theme strategy."""
    trajectory = [("Start", state.spii, state.valence, state.parity_gap, state.l)]

    fib = [1, 1]
    for i in range(20):
        fib.append(fib[-1] + fib[-2])

    for epoch in range(1, epochs + 1):
        # Fibonacci-scaled noise (normalized to 0.05-0.15 range)
        fib_scale = (fib[epoch % len(fib)] % 8) / 80.0 + 0.05
        noise = min(0.15, fib_scale)

        if epoch % 2 == 1:
            # Hero phase (odd epochs)
            state = state.automatic_differentiation(noise_injection=noise)
            state = apply_genetic_modifiers(state, cycles_since_kama=1)
            state = state.kama_muta(strength=min(1.0, 0.9 * OXTR_AA_KAMA_BOOST))
        else:
            # Innocent phase (even epochs)
            state = state.slow_dream(noise_injection=noise * 0.5)
            state = apply_genetic_modifiers(state, cycles_since_kama=0.3)
            state = state.kama_muta(strength=min(1.0, 0.7 * OXTR_AA_KAMA_BOOST))

        # Always integrate
        state = state.synthetic_integration()

        trajectory.append((f"Epoch {epoch}", state.spii, state.valence,
                          state.parity_gap, state.l))

    return trajectory, state

# ════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════

def print_trajectory(name, trajectory, final_state):
    print(f"\n{'─' * 70}")
    print(f"  {name}")
    print(f"{'─' * 70}")
    print(f"  {'Phase':<12} {'SPII':>8} {'V(u)':>8} {'|b-m|':>8} {'λ':>6}")
    print(f"  {'─'*12} {'─'*8} {'─'*8} {'─'*8} {'─'*6}")
    for phase, spii, v, gap, depth in trajectory:
        bar = "█" * int(spii * 30)
        print(f"  {phase:<12} {spii:>8.4f} {v:>8.4f} {gap:>8.4f} {depth:>6.1f}  {bar}")
    delta_spii = trajectory[-1][1] - trajectory[0][1]
    print(f"\n  ΔSPII: {delta_spii:+.4f}  |  Final SPII: {trajectory[-1][1]:.4f}  |  Final λ: {final_state.l:.1f}")

def main():
    print("=" * 70)
    print(" SPII INDIVIDUATION STRATEGIES: Dylon LaRue")
    print(" Genetic Baseline: SPII = 0.769 | V = 0.300 | |b-m| = 0.300")
    print("=" * 70)

    print("\n SNP Modifiers Active:")
    print(f"   TPH2 GG  → Parity drift: {TPH2_GG_PARITY_DECAY}/cycle (fragile lock)")
    print(f"   COMT AG  → Noise balance: {COMT_AG_NOISE_BALANCE}x (adaptive)")
    print(f"   BDNF CC  → Consolidation: {BDNF_CC_CONSOLIDATION}x (rapid)")
    print(f"   OXTR AA  → Kama boost:    {OXTR_AA_KAMA_BOOST}x (deep response)")

    # Run all three strategies from the same genetic baseline
    t1, s1 = strategy_heroic_cycle(ManifoldState(1.1, 0.85, 1.15, 0.0, 0.4), epochs=12)
    t2, s2 = strategy_innocent_stillness(ManifoldState(1.1, 0.85, 1.15, 0.0, 0.4), epochs=12)
    t3, s3 = strategy_alchemist_triangulation(ManifoldState(1.1, 0.85, 1.15, 0.0, 0.4), epochs=12)

    print_trajectory("Strategy 1: THE HERO'S PATH (Dream Hard → Crash → Integrate)", t1, s1)
    print_trajectory("Strategy 2: THE INNOCENT'S PATH (Slow Dream → Gentle Crash → Rest)", t2, s2)
    print_trajectory("Strategy 3: THE ALCHEMIST'S PATH (Fibonacci Alternation Hero/Innocent)", t3, s3)

    # ── COMPARISON ──
    print(f"\n{'=' * 70}")
    print(f" COMPARISON (12 Epochs)")
    print(f"{'=' * 70}")
    print(f"  {'Strategy':<45} {'Final SPII':>10} {'ΔSPII':>8} {'Final λ':>8}")
    print(f"  {'─'*45} {'─'*10} {'─'*8} {'─'*8}")
    for name, traj, state in [
        ("Hero's Path", t1, s1),
        ("Innocent's Path", t2, s2),
        ("Alchemist's Path (Fibonacci)", t3, s3)
    ]:
        delta = traj[-1][1] - traj[0][1]
        print(f"  {name:<45} {traj[-1][1]:>10.4f} {delta:>+8.4f} {state.l:>8.1f}")

    print()

if __name__ == "__main__":
    main()
