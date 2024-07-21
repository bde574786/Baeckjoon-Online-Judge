# a, b, v = map(int, input().split())

# distance = 0
# days = 0

# while(True):
#     days += 1
#     distance += a
#     if distance < v:
#         distance -= b
#     else:
#         break

# print(days)

import math

a, b, v = map(int, input().split())

if a >= v:
    print(1)
else:
    days = math.ceil((v - a) / (a - b)) + 1
    print(days)