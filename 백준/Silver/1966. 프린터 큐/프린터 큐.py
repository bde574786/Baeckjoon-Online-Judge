from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))

    queue = deque((i, doc[i]) for i in range(n))
    print_order = 0
    
    while queue:
        current = queue.popleft()
        if any(current[1] < other[1] for other in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[0] == m:
                print(print_order)
                break