import math
import time

def factorize(n):
    factors = {}
    d = 2
    limit = math.isqrt(n)
    while d <= limit:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

t0 = time.time()
for i in range(1000):
    factorize(136279840 + i)
t1 = time.time()
print(f"Factored 1000 numbers near 1.36e8 in {t1-t0:.4f} seconds.")
