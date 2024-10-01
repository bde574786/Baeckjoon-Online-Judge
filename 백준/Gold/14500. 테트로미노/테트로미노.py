n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
visited = [[False] * m for _ in range(n)]

# dfs
def dfs(x, y, count, total):
    global result
    
    if count == 4:
        result = max(result, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, count + 1, total + graph[ny][nx])
            visited[ny][nx] = False  # backtracking

# `ㅗ' 모양: 4가지 방향 동시 탐색
def check_t_shape(x, y):
    global result
    
    total = graph[y][x]
    sums = []
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            sums.append(graph[ny][nx])
        
    if len(sums) >= 4:
        result = max(result, total + sum(sums) - min(sums))
    elif len(sums) == 3:
        result = max(result, total + sum(sums))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, 1, graph[i][j])
        visited[i][j] = False
        check_t_shape(j, i)

print(result)
