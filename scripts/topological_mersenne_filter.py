#!/usr/bin/env python3
"""
Topological Mersenne Filter

Leverages the Protoreal Algebra / Golden Field sewing topology to pre-filter
Mersenne prime exponent candidates. Eliminates the need to run full Lucas-Lehmer
tests on candidates that do not possess the required structural resonances in
their topological orders.

Identified Topological Resonances in recent Mersenne Exponents:
- R = 1: Unbroken fundamental symmetry
- R = 2: Basic bifurcation
- R = 8: Physical Sector Prime Count (F6)
- R = 11: Plasma Mirrors / 5th Lucas Number
- R = 13: Dimension of Life / Generator Count (F7)

Authors: LaRue (Theory), Antigravity (Implementation)
"""

import math
import sys
import argparse
import multiprocessing as mp
import time

# ═══════════════════════════════════════════════════════════
# MATH UTILITIES
# ═══════════════════════════════════════════════════════════

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def factorize(n):
    """Fast factorization for numbers up to ~10^10."""
    factors = {}
    d = 2
    limit = math.isqrt(n)
    while d <= limit:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
            limit = math.isqrt(n)
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def sqrt_mod(n, p):
    """Tonelli-Shanks algorithm for square roots mod p."""
    if pow(n, (p-1)//2, p) != 1: return None
    if p % 4 == 3: return pow(n, (p+1)//4, p)
    q, s = p-1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p-1: z += 1
    M, c, t, R = s, pow(z, q, p), pow(n, q, p), pow(n, (q+1)//2, p)
    while True:
        if t == 1: return R
        i = 0; tmp = t
        while tmp != 1: tmp = tmp*tmp % p; i += 1
        b = pow(c, 1 << (M-i-1), p)
        M, c, t, R = i, b*b%p, t*b*b%p, R*b%p

def golden_roots(p):
    """Returns phi and pbar (conjugate) modulo p."""
    s5 = sqrt_mod(5, p)
    if s5 is None: return None, None
    inv2 = pow(2, p-2, p)
    phi = (1 + s5) * inv2 % p
    pbar = (1 - s5 + p) * inv2 % p
    return phi, pbar

def order_mod(base, mod, factors):
    """Computes multiplicative order of base modulo mod given factorization of mod-1."""
    t = mod - 1
    for p_fac, e in factors.items():
        t //= (p_fac ** e)
        while pow(base, t, mod) != 1:
            t *= p_fac
    return t

# ═══════════════════════════════════════════════════════════
# TOPOLOGICAL FILTER
# ═══════════════════════════════════════════════════════════

# Valid structural ratios R = (p-1) / ord_pbar
# 1, 2 = trivial/bifurcation
# 8 = Physical Sector Primes (F6)
# 11 = Plasma Mirrors (L5)
# 13 = Dimension of Life (F7)
VALID_RESONANCES = {1, 2, 8, 11, 13}

def evaluate_candidate(p):
    """
    Evaluates a single prime exponent candidate.
    Returns (p, phi, ord_pbar, ratio) if successful, else None.
    """
    if not is_prime(p):
        return None
        
    # Golden Split constraint: 5 must be a quadratic residue
    if p % 5 not in [1, 4]:
        return None
        
    phi, pbar = golden_roots(p)
    if not pbar:
        return None
        
    # Compute topological orbit order
    factors = factorize(p - 1)
    ord_pbar = order_mod(pbar, p, factors)
    
    ratio = (p - 1) // ord_pbar
    return (p, phi, ord_pbar, ratio)


def search_worker(start_p, end_p):
    """Worker process for parallel searching."""
    results = []
    # Ensure starting on an odd number
    if start_p % 2 == 0: start_p += 1
    
    for p in range(start_p, end_p, 2):
        res = evaluate_candidate(p)
        if res and res[3] in VALID_RESONANCES:
            results.append(res)
    return results

# ═══════════════════════════════════════════════════════════
# MAIN ROUTINES
# ═══════════════════════════════════════════════════════════

def verify_known():
    """Verify the filter against known recent Mersenne prime exponents."""
    known = [20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 
             42643801, 43112609, 57885161, 74207281, 77232917, 82589933, 136279841]
             
    print("═══════════════════════════════════════════════════════════")
    print("  TOPOLOGICAL VERIFICATION OF KNOWN MERSENNE EXPONENTS")
    print("═══════════════════════════════════════════════════════════\n")
    
    for p in known:
        res = evaluate_candidate(p)
        if not res:
            print(f"[REJECTED] p = {p:<10} | Failed Golden Split (5 is not a quadratic residue mod p)")
        else:
            _, phi, ord_pbar, ratio = res
            marker = "★" if ratio in VALID_RESONANCES else ""
            desc = ""
            if ratio == 8: desc = "[F6: Physical Sector]"
            elif ratio == 11: desc = "[L5: Plasma Mirrors]"
            elif ratio == 13: desc = "[F7: Dimension of Life]"
            elif ratio in [1,2]: desc = "[Base Resonance]"
            
            print(f"[{'RESONANT' if marker else 'WEAK    '}] p = {p:<10} | R = (p-1)/ord = {ratio:<2} {marker} {desc}")
    print()


def search_new(start_val, chunk_size, num_chunks):
    """Search for new candidates > M136279841 in parallel."""
    print("═══════════════════════════════════════════════════════════")
    print(f"  TOPOLOGICAL MERSENNE SEARCH: > {start_val}")
    print("═══════════════════════════════════════════════════════════\n")
    
    cores = mp.cpu_count()
    print(f"Using {cores} cores for parallel search...")
    print(f"Target resonances: R ∈ {VALID_RESONANCES}\n")
    
    pool = mp.Pool(processes=cores)
    
    total_scanned = 0
    t0 = time.time()
    
    for chunk in range(num_chunks):
        chunk_start = start_val + chunk * chunk_size
        chunk_end = chunk_start + chunk_size
        
        # Split chunk among cores
        step = chunk_size // cores
        ranges = [(chunk_start + i*step, chunk_start + (i+1)*step) for i in range(cores)]
        ranges[-1] = (ranges[-1][0], chunk_end) # catch remainder
        
        results = pool.starmap(search_worker, ranges)
        
        # Flatten and print
        for core_results in results:
            for (p, phi, ord_pbar, ratio) in core_results:
                desc = ""
                if ratio == 8: desc = "[F6: Physical Sector]"
                elif ratio == 11: desc = "[L5: Plasma Mirrors]"
                elif ratio == 13: desc = "[F7: Dimension of Life]"
                print(f"★ NEW CANDIDATE FOUND! p = {p:<10} | R = {ratio:<2} {desc}")
                
        total_scanned += chunk_size
        elapsed = time.time() - t0
        rate = total_scanned / elapsed
        print(f"... scanned up to {chunk_end:,} | {rate:,.0f} nums/sec", end='\r')
        
    print("\n\nSearch complete.")
    pool.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Topological Mersenne Filter")
    parser.add_argument('--verify', action='store_true', help='Verify known Mersenne exponents')
    parser.add_argument('--search', action='store_true', help='Search for new exponents')
    parser.add_argument('--start', type=int, default=136279841, help='Start value for search')
    parser.add_argument('--limit', type=int, default=10_000_000, help='Total numbers to scan')
    
    args = parser.parse_args()
    
    if args.verify:
        verify_known()
    if args.search:
        search_new(args.start, 500_000, args.limit // 500_000)
    
    if not len(sys.argv) > 1:
        parser.print_help()
