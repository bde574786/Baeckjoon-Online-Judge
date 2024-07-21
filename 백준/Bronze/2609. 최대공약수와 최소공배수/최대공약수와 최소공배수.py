# a, b = map(int, input().split())

# a_divisor = {i for i in range(1, a+1) if a % i == 0}
# b_divisor = {i for i in range(1, b+1) if b % i == 0}

# common_divisors = list(a_divisor & b_divisor)
# print(max(common_divisors))

# greater = max(a, b)

# while True:
#     if greater % a == 0 and greater % b == 0:
#         common_multiple = greater
#         break
#     greater += 1
    
# print(common_multiple)

import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))