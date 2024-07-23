n = int(input())
sizes = []
ranks = [1] * n

for i in range(n):
    x, y = map(int, input().split())
    sizes.append((x, y))

for i in range(n):
    for j in range(n):
        if i != j:
            if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]:
                ranks[i] += 1

for i in ranks:
    print(i, end = ' ')
