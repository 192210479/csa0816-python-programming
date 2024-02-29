from functools import reduce
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input("N value: "))
numbers = [int(input(f"Number {i}: ")) for i in range(1, n + 1)]

lcm_result = reduce(lcm, numbers)
gcd_result = reduce(gcd, numbers)

print("LCM =", lcm_result)
print("GCD =",gcd_result)
