import math

arc_1 = 2 * math.pi / 19
print(f"Arc of 1 segment = {arc_1} (approx 1/3 = {1/3})")

arc_3 = 3 * arc_1
print(f"Arc of 3 segments (4 points) = {arc_3} (approx 1)")

arc_6 = 6 * arc_1
print(f"Arc of 6 segments (7 points) = {arc_6} (approx 2)")

# Difference between 3 segments and unit arc
diff = 1 - arc_3
print(f"Diff between 3 segments and 1 radian = {diff}")

phi = (1 + math.sqrt(5)) / 2
print(f"Diff * 100 = {diff * 100}")
print(f"Diff * 19 = {diff * 19}")

