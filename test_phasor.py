import re

with open("os.path.join(os.path.dirname(__file__), "LaRueProtorealAlgebra/PhasorTower.lean")", "r") as f:
    content = f.read()
    
# Find where to append the new theorem
print(content[-500:])
