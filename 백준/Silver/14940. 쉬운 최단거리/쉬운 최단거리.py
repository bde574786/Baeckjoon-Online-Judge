from collections import deque

def bfs(n, m, graph):
    distance = [[-1] * m for _ in range(n)]
    queue = deque()
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                distance[i][j] = 0

    return distance

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = bfs(n, m, graph)

for i in result:
    print(' '.join(map(str, i)))