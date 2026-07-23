import math

# New Prime Gauge Triangle
a, b, c = 119, 181, 229
perimeter = a + b + c
s = perimeter / 2
area_sq = s * (s - a) * (s - b) * (s - c)
area = math.sqrt(area_sq)

print(f"Perimeter: {perimeter} ({math.sqrt(perimeter)}^2)")
print(f"Semiperimeter: {s}")
print(f"Area^2: {area_sq}")
print(f"Area: {area}")

# Is there a close integer for Area?
print(f"Area approximation: 10680.75 ? {10680.75**2 == area_sq}")

# Fine structure constant alpha ≈ 1/137.035999
alpha_inv = 137.035999084
alpha = 1 / alpha_inv

# Could area relate to alpha?
print(f"Area / (a*b) = {area / (a*b)}")
print(f"c / Area = {c / area}")

# What about the Riemann Zeta values?
# Turok mirror projection: c^2 - (a^2 + b^2)
obtuse_defect = c**2 - (a**2 + b**2)
print(f"Obtuse Defect (c^2 - a^2 - b^2) = {obtuse_defect}")
print(f"sqrt(Defect) = {math.sqrt(obtuse_defect)}")
print(f"Defect / 137 = {obtuse_defect / 137}")

# Check beta angles
import itertools
for num in [a, b, c, perimeter, obtuse_defect]:
    print(f"atan(Area / {num}) = {math.atan(area / num)}")

print(f"pi / atan(Area / obtuse_defect) = {math.pi / math.atan(area / obtuse_defect)}")
