from collections import deque

def bfs(m, n, h, box):
    queue = deque()
    days = -1
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append((i, j, k))
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            
            for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                
                if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:  #  if unripe
                    box[nx][ny][nz] = 1  # ripe
                    queue.append((nx, ny, nz))
    
    for i in range(h):
        for j in range(n):
            if 0 in box[i][j]:
                return -1
    
    return days

m, n, h = map(int, input().split())
box = [[[0]*m for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, input().split()))

result = bfs(m, n, h, box)
print(result)