import math

radian = 180 / math.pi
phi = (1 + math.sqrt(5)) / 2

# 6 consecutive points = 5 segments
segments = 5

arc_length = segments * 2 * math.pi / 19
chord = 2 * math.sin(segments * math.pi / 19)
angle = segments * 360 / 19

print(f"6 points (5 segments):")
print(f"Arc length = {arc_length}")
print(f"Chord length = {chord}")
print(f"Angle = {angle} degrees")

print(f"\nUnit arc (radian) = {radian}")
print(f"Phi = {phi}")
print(f"1/Phi = {1/phi}")

# Check connections
print(f"\nConnections:")
print(f"Arc length * Phi = {arc_length * phi}")
print(f"Arc length / Phi = {arc_length / phi}")
print(f"Chord * Phi = {chord * phi}")
print(f"Chord / Phi = {chord / phi}")

# What if 6 segments?
print(f"\nWhat about 6 segments (7 points)?")
arc_6 = 6 * 2 * math.pi / 19
chord_6 = 2 * math.sin(6 * math.pi / 19)
print(f"Arc length = {arc_6}")
print(f"Chord length = {chord_6}")

# Since 6 * pi ~= 19, 
# 6 * pi / 19 ~= 1
# So 3 * 2 * pi / 19 ~= 1
print(f"\nSince 6*pi ~ 19:")
print(f"3 segments (4 points) arc length = {3 * 2 * math.pi / 19}")

