import math

phi = (1 + math.sqrt(5)) / 2

# Distance between 5 consecutive points means the chord spanning 4 edges
chord_4 = 2 * math.sin(4 * math.pi / 19)
print(f"Chord spanning 4 edges: {chord_4}")

# Chord spanning 5 edges (6 points)
chord_5 = 2 * math.sin(5 * math.pi / 19)
print(f"Chord spanning 5 edges: {chord_5}")

# Sum of 4 chords
sum_4 = 4 * 2 * math.sin(math.pi / 19)
print(f"Sum of 4 chords: {sum_4}")

# Sum of 5 chords
sum_5 = 5 * 2 * math.sin(math.pi / 19)
print(f"Sum of 5 chords: {sum_5}")

print(f"Phi = {phi}")

# Check connections
print(f"Chord_4 / Unit arc (1) = {chord_4}")
print(f"Chord_5 / Unit arc (1) = {chord_5}")
print(f"sum_4 / Phi = {sum_4 / phi}")
print(f"sum_5 / Phi = {sum_5 / phi}")

# User said "the unit arc overlays the distance between any 5 consecutive points of an inscribed 19-gon"
# If unit arc = 1, then the distance = 1 ?
# What distance between 5 points is exactly 1?
# Maybe the product of distances?
# Product of diagonals from P0 to P1, P2, P3, P4?
prod = 1
for k in range(1, 5):
    prod *= 2 * math.sin(k * math.pi / 19)
print(f"Product of 4 diagonals: {prod}")
print(f"Product of 5 diagonals: {prod * 2 * math.sin(5 * math.pi / 19)}")

