from collections import deque

def dfs(graph, start, visited):
       visited[start] = True
       result.append(start)
       for neighbor in graph[start]:
              if not visited[neighbor]:
                     dfs(graph, neighbor, visited)
       

def bfs(graph, start, visited):
       queue = deque([start])
       visited[start] = True
       while queue:
              current = queue.popleft()
              result.append(current)
              for neighbor in graph[current]:
                     if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
       a, b = map(int, input().split())
       graph[a].append(b)
       graph[b].append(a)
       
for i in graph:
       i.sort()

# dfs
visited = [False] * (n + 1)
result = []
dfs(graph, v, visited)
print(' '.join(map(str, result)))

# bfs
visited = [False] * (n + 1)
result = []
bfs(graph, v, visited)
print(' '.join(map(str, result)))