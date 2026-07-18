#!/usr/bin/env python3
"""
Monster Fermat Topological Prime Generator

Uses the Monster Fermat Equation:
E(n) = 6 * a^n + 7 * b^n ± 89
where a and b are gauge flavors (default 5 and 6).

This script sieves candidate exponents `n` by evaluating E(n) modulo
small primes to quickly eliminate composite candidates before performing
full probabilistic primality testing.

Authors: LaRue (Theory), Antigravity (Implementation)
"""

import sys
import argparse
import multiprocessing as mp
import time

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def get_small_primes(limit):
    sieve = [True] * (limit + 1)
    for x in range(3, int(limit**0.5) + 1, 2):
        if sieve[x]:
            for y in range(x * x, limit + 1, x * 2):
                sieve[y] = False
    return [2] + [i for i in range(3, limit + 1, 2) if sieve[i]]

# Precompute small primes for the sieve
SMALL_PRIMES = get_small_primes(5000)

def topological_factor_check(n, a, b, sign):
    """
    Checks if E(n) = 6*a^n + 7*b^n + sign*89 has a small prime factor.
    Returns the factor if composite, else None.
    """
    for q in SMALL_PRIMES:
        if q == a or q == b:
            # If q divides a or b, the mod doesn't cycle simply, evaluate directly
            val = (6 * pow(a, n, q) + 7 * pow(b, n, q) + sign * 89) % q
        else:
            val = (6 * pow(a, n, q) + 7 * pow(b, n, q) + sign * 89) % q
        if val == 0:
            return q
    return None

def miller_rabin(n, k=5):
    """Simple probabilistic primality test for large numbers."""
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
        
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
        
    # We use a fixed set of bases for deterministic checking up to a point,
    # but for very large numbers we just do a few rounds.
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a_base in bases[:k]:
        if n <= a_base:
            break
        x = pow(a_base, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def search_worker(start_n, end_n, a, b):
    """Worker process for parallel searching."""
    candidates = []
    
    for n in range(start_n, end_n):
        for sign in [1, -1]:
            # Sieve by small primes first (very fast)
            factor = topological_factor_check(n, a, b, sign)
            if factor is None:
                # If it passes the sieve, do a full evaluation
                E_n = 6 * (a ** n) + 7 * (b ** n) + sign * 89
                
                # Fast probable prime check
                if miller_rabin(E_n, k=3): 
                    candidates.append((n, sign, E_n))
                    
    return candidates

def search_new(start_val, limit, a, b):
    """Search for new prime candidates in parallel."""
    print("═══════════════════════════════════════════════════════════")
    print(f"  MONSTER FERMAT TOPOLOGICAL PRIME SEARCH")
    print(f"  Function: E(n) = 6 * {a}^n + 7 * {b}^n ± 89")
    print("═══════════════════════════════════════════════════════════\n")
    
    cores = mp.cpu_count()
    print(f"Using {cores} cores for parallel search...")
    print(f"Sieving with primes < 5000\n")
    
    pool = mp.Pool(processes=cores)
    
    total_scanned = 0
    t0 = time.time()
    
    chunk_size = 1000
    num_chunks = limit // chunk_size
    if num_chunks == 0:
        num_chunks = 1
        chunk_size = limit
    
    for chunk in range(num_chunks):
        chunk_start = start_val + chunk * chunk_size
        chunk_end = chunk_start + chunk_size
        
        step = max(1, chunk_size // cores)
        ranges = [(chunk_start + i*step, chunk_start + (i+1)*step, a, b) for i in range(cores)]
        ranges[-1] = (ranges[-1][0], chunk_end, a, b)
        
        results = pool.starmap(search_worker, ranges)
        
        for core_results in results:
            for n, sign, E_n in core_results:
                sign_str = "+" if sign > 0 else "-"
                print(f"★ NEW PROBABLE PRIME FOUND! E({n}) = 6*{a}^{n} + 7*{b}^{n} {sign_str} 89")
                
        total_scanned += chunk_size
        elapsed = time.time() - t0
        rate = total_scanned / elapsed if elapsed > 0 else 0
        print(f"... scanned up to n = {chunk_end:,} | {rate:,.0f} exponents/sec", end='\r')
        
    print("\n\nSearch complete.")
    pool.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monster Fermat Prime Generator")
    parser.add_argument('--start', type=int, default=1, help='Start exponent n')
    parser.add_argument('--limit', type=int, default=10000, help='Total exponents to scan')
    parser.add_argument('-a', type=int, default=5, help='Base a (default 5)')
    parser.add_argument('-b', type=int, default=6, help='Base b (default 6)')
    
    args = parser.parse_args()
    search_new(args.start, args.limit, args.a, args.b)
