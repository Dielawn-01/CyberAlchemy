import math

# Unit arc in degrees
unit_arc = 180 / math.pi
print(f"Unit arc = {unit_arc}")

# 19-gon angles
for i in range(1, 20):
    print(f"Angle {i}: {i * 360 / 19}")

# User says: unit arc overlays the distance between any 5 consecutive points.
# 5 consecutive points means points 0, 1, 2, 3, 4. (4 segments)
# What is the distance? 
# Maybe Euclidean distance between P0 and P3 (which is 4 points, 3 segments) = 0.951
# Maybe the arc length between P0 and P3 = 0.992

# Golden ratio connection:
# (1 + sqrt(5))/2 = 1.618
# (1 - sqrt(5))/2 = -0.618

