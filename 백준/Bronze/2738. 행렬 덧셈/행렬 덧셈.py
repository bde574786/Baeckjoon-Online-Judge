n, m = map(int, input().split())

a, b = [], []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

c = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j] + b[i][j])
    c.append(row)
    
for row in c:
    print(' '.join(map(str, row)))