a, b, c = map(int, input().split())

sides = sorted([a, b, c])

while sides[0] + sides[1] <= sides[2]:
    sides[2] -= 1

print(sum(sides))
