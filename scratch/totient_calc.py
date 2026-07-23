import math
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

sq10 = 10**2
sq19 = 19**2

phi10 = phi(sq10)
phi19 = phi(sq19)

print(f"phi(10^2) = {phi10}")
print(f"phi(19^2) = {phi19}")
print(f"Ratio phi(19^2)/phi(10^2) = {phi19/phi10}")
print(f"Ratio phi(10^2)/phi(19^2) = {phi10/phi19}")
print(f"Difference = {phi19 - phi10}")
print(f"Product = {phi19 * phi10}")

print(f"180/pi = {180/math.pi}")
print(f"361 / (2 * pi) = {361/(2*math.pi)}")

