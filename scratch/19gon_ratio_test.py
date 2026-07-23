import math

phi = (1 + math.sqrt(5)) / 2

diagonals = []
for i in range(1, 10):
    diagonals.append(2 * math.sin(i * math.pi / 19))

print(f"Phi = {phi}")

for i in range(len(diagonals)):
    for j in range(len(diagonals)):
        if i != j:
            ratio = diagonals[i] / diagonals[j]
            diff = abs(ratio - phi)
            if diff < 0.05:
                print(f"d_{i+1} / d_{j+1} = {ratio} (diff to Phi: {diff})")

