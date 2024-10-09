from collections import deque

def bfs(n, k):
       visited = [False] * 100001
       queue = deque([(n, 0)]) # (current_pos, current_time)
       visited[n] = True
       
       while queue:
              current_pos, current_time = queue.popleft()
              if current_pos == k:
                     return current_time
       
              move = [current_pos - 1, current_pos + 1, current_pos*2] # same level node
              
              for i in move:
                     if 0 <= i <= 100000 and not visited[i]:
                            visited[i] = True
                            queue.append((i, current_time + 1))

n, k = map(int, input().split())
print(bfs(n, k))