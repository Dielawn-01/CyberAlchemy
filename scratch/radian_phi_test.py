import math

radian = 180 / math.pi
phi = (1 + math.sqrt(5)) / 2
conj_phi = (1 - math.sqrt(5)) / 2

# 19-gon angles
for k in range(1, 10):
    angle = k * 360 / 19
    diff = radian - angle
    print(f"k={k}, angle={angle}, diff={diff}")
    
    # Check if diff relates to phi
    print(f"  diff / phi = {diff / phi}")
    print(f"  diff * phi = {diff * phi}")
    print(f"  diff - (phi/k) = {diff - (phi/k)}")
    
