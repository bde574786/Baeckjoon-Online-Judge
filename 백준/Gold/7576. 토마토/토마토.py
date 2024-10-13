from collections import deque

def bfs(m, n ,box):
    queue = deque()
    days = -1
    
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:  # if unripe
                    box[nx][ny] = 1  # ripe
                    queue.append((nx, ny))
    
    for i in box:
        if 0 in i:
            return -1
    
    return days

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

result = bfs(m, n, box)
print(result) 