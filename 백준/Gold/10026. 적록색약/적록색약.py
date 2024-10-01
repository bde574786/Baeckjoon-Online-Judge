import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())

def dfs(x, y, color):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == color:
            dfs(nx, ny, color)
            
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 적록색약이 아닌 dfs
normal_count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            normal_count += 1

# 적록색약 그래프
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

# 적록색약 dfs
colorblind_count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            colorblind_count += 1


print(normal_count, colorblind_count)
