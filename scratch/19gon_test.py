import math

phi = (1 + math.sqrt(5)) / 2
print(f"Golden Ratio (Phi) = {phi}")

radius = 1
angle_step = 2 * math.pi / 19

print("\nChord lengths from P0:")
for i in range(1, 10):
    angle = i * angle_step
    chord = 2 * radius * math.sin(angle / 2)
    print(f"  P0 to P{i}: {chord}")

print("\nArc lengths from P0:")
for i in range(1, 10):
    arc = i * angle_step
    print(f"  P0 to P{i}: {arc}")

print("\nSum of chord lengths:")
side = 2 * math.sin(math.pi / 19)
for i in range(1, 10):
    print(f"  {i} sides: {i * side}")
