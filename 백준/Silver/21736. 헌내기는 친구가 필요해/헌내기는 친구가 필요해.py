import sys
sys.setrecursionlimit(10**6) 

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

start_x, start_y = 0, 0
found = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            start_x, start_y = i, j
            found = True
            break
    
    if found:
        break


visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    result = 0
    
    if graph[x][y] == 'P':
        result += 1
        
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] != 'X':
                result += dfs(nx, ny)
    
    return result

result = dfs(start_x, start_y)

print(result if result != 0 else "TT")