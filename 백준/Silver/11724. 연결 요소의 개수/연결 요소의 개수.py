import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, visited, v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1

print(count)