import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    visited = [-1] * (len(graph))
    queue = deque([start])
    visited[start] = 0
    
    distance = 0
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + 1
                distance += visited[i]
                
    return distance

min_bacon = sys.maxsize
result = 0
for i in range(1, n + 1):
    bacon = bfs(graph, i)
    if bacon < min_bacon:
        min_bacon = bacon
        result = i
    elif bacon == min_bacon:
        if i < result:
            result = i

print(result)
