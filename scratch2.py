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

def multiplicative_order(base, mod):
    if base % mod == 0: return 0
    x, order = base % mod, 1
    # For large primes, this is too slow. We need factorization of p-1.
    return None

mersenne_exponents = [
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609, 57885161, 74207281, 77232917, 82589933, 136279841
]

for p in mersenne_exponents[-10:]:
    res5 = pow(5, (p-1)//2, p) if p > 2 else 0
    print(f"p={p}, p%5={p%5}, p%6={p%6}, 5 is QR? {res5 == 1}")

