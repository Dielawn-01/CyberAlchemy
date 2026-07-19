import math

def sqrt_mod(n, p):
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
    s5 = sqrt_mod(5, p)
    if s5 is None: return None
    inv2 = pow(2, p-2, p)
    phi = (1 + s5) * inv2 % p
    pbar = (1 - s5 + p) * inv2 % p
    return phi, pbar

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def order_mod(base, mod, factors):
    t = mod - 1
    for p_fac, e in factors.items():
        t //= (p_fac ** e)
        # multiply back p_fac until pow != 1
        while pow(base, t, mod) != 1:
            t *= p_fac
    return t

mersenne_exponents = [
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609, 57885161, 74207281, 77232917, 82589933, 136279841
]

for p in mersenne_exponents[-15:]:
    if p % 5 not in [1, 4]:
        continue # No golden split
    roots = golden_roots(p)
    if not roots: continue
    phi, pbar = roots
    factors = factorize(p - 1)
    ord_phi = order_mod(phi, p, factors)
    ord_pbar = order_mod(pbar, p, factors)
    print(f"p={p:<10} | phi={phi:<10} | ord_pbar={ord_pbar:<10} | (p-1)/ord_pbar = {(p-1)//ord_pbar}")

