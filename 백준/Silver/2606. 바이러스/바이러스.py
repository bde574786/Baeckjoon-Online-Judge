import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n + 1)
start = 1
queue = [start]
visited[start] = True
count = 0

while queue:
    node = queue.pop(0)
    count += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            queue.append(neighbor)
            visited[neighbor] = True

print(count - 1)