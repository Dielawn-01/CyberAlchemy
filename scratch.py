def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

p = 136279841
print(f"p = {p}")
print(f"is_prime: {is_prime(p)}")
print(f"p % 5 = {p % 5}")
print(f"p % 6 = {p % 6}")
