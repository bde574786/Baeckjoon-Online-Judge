import sys

n = int(input())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

for i in sorted_points:
    print(i[0], i[1])