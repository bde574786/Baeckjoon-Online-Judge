import sys

input = sys.stdin.readline
m = int(input())

result_set = set()
for _ in range(m):
    command = input().strip().split()
    action = command[0]
    
    if len(command) > 1:
        value = int(command[1])
    
    if action == 'add':
        result_set.add(value)
    elif action == 'remove':
        result_set.discard(value)
    elif action == 'check':
        print(1 if value in result_set else 0)
    elif action == 'toggle':
        if value in result_set:
            result_set.remove(value)
        else:
            result_set.add(value)
    elif action == 'all':
        result_set = set(range(1, 21))
    elif action == 'empty':
        result_set.clear()
