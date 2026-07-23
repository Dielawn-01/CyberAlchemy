import math

radian = 180 / math.pi
phi = (1 + math.sqrt(5)) / 2

# Check if radian can be constructed with phi, 19, 5
# User said "distance between any 5 consecutive points"
# Distance could be the angle: 4 * 360 / 19 = 75.78947, or 5 * 360 / 19 = 94.7368
# Let's check difference
angle_4 = 4 * 360 / 19
angle_5 = 5 * 360 / 19

# Maybe the connection is through the trig functions
# The Golden ratio is 2 * cos(pi/5)
# So pi/5 is related to phi.
# 180 / pi = (360/19) * f(phi) ?

print(f"Radian = {radian}")
print(f"Angle 4 (5 points) = {angle_4}")
print(f"Angle 5 (6 points) = {angle_5}")
print(f"Phi = {phi}")

# Check phi * angle_4 ?
print(f"Angle_4 / Phi = {angle_4 / phi}")
print(f"Angle_4 * Phi = {angle_4 * phi}")

# What if "distance" means physical distance (chord)?
d4 = 2 * math.sin(4 * math.pi / 19)
d5 = 2 * math.sin(5 * math.pi / 19)
print(f"d4 = {d4}")
print(f"d5 = {d5}")

# Unit arc = 1 radian (angle), or 1 (length)?
# If the unit arc is 1, and it overlays the distance...
# Maybe distance = d4 * phi ?
print(f"d4 * phi = {d4 * phi}")
print(f"d4 / phi = {d4 / phi}")

