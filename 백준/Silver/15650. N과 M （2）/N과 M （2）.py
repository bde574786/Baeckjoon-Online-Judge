from itertools import combinations

n, m = map(int, input().split())

combs = combinations(range(1, n+1), m)

for i in combs:
    print(" ".join(map(str, i)))