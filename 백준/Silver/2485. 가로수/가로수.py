import math

n = int(input())
trees = [int(input()) for _ in range(n)]

gaps = []
for i in range(1, n):
    gaps.append(trees[i] - trees[i - 1])

gcd_value = gaps[0]
for i in range(1, len(gaps)):
    gcd_value = math.gcd(gcd_value, gaps[i])

new_trees = 0
for gap in gaps:
    new_trees += (gap // gcd_value) - 1

print(new_trees)
