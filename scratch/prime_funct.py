import sympy

primes = [19, 139, 181, 229, 14489]

for p in primes:
    print(f"pi({p}) = {sympy.primepi(p)}")

