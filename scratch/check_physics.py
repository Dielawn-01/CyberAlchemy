import math
from fractions import Fraction

def mult_order(a, p):
    if a % p == 0: return 0
    for k in range(1, p):
        if pow(a, k, p) == 1:
            return k
    return p - 1

# Old Lockwood Triangle
old_sides = (116, 138, 144)
s_old = sum(old_sides) / 2
area_old_sq = s_old * (s_old - old_sides[0]) * (s_old - old_sides[1]) * (s_old - old_sides[2])
print(f"Old Triangle {old_sides}: Perimeter = {sum(old_sides)}, Area^2 = {area_old_sq}")

# New Prime Gauge Triangle
new_sides = (119, 181, 229)
s_new = sum(new_sides) / 2
area_new_sq = s_new * (s_new - new_sides[0]) * (s_new - new_sides[1]) * (s_new - new_sides[2])
print(f"New Triangle {new_sides}: Perimeter = {sum(new_sides)} = {sum(new_sides)**0.5}^2, Area^2 = {area_new_sq}")

print("\nMultiplicative orders mod 229:")
for x in new_sides:
    print(f"ord({x} mod 229) = {mult_order(x, 229)}")

print("\nMultiplicative orders mod 181:")
for x in new_sides:
    print(f"ord({x} mod 181) = {mult_order(x, 181)}")

print("\nMultiplicative orders mod 139:")
for x in new_sides:
    print(f"ord({x} mod 139) = {mult_order(x, 139)}")

# Fine Structure Constant approximation
print("\nFine Structure Constant checks:")
# 14489 is the bridge prime
bridge_prime = 14489
for x in new_sides:
    if x != 0:
        print(f"14489 mod {x} = {bridge_prime % x}")
print(f"14489 mod {119-2} = {bridge_prime % (119-2)}")
