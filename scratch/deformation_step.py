import math

phi = (1 + math.sqrt(5)) / 2
deformation = phi / (2 * math.pi)

print(f"Phi = {phi}")
print(f"2*pi = {2 * math.pi}")
print(f"Deformation step (Phi / 2pi) = {deformation}")

# Let's check 1 / deformation
print(f"Inverse deformation = {1 / deformation}")
print(f"1 / deformation^2 = {1 / (deformation**2)}")

# Let's check relation to 229 and 14489
print(f"229 * deformation = {229 * deformation}")
print(f"14489 * deformation = {14489 * deformation}")

# What about the radian? 180 / pi
radian = 180 / math.pi
print(f"Radian = {radian}")
print(f"Radian / deformation = {radian / deformation}")

# Wait, Radian = 360 / (2 * pi). Deformation = phi / (2 * pi)
# Radian / Deformation = 360 / phi
print(f"360 / Phi = {360 / phi}")
print(f"360 * Phi = {360 * phi}")

