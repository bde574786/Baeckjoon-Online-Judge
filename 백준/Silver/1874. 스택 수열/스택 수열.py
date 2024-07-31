import sys

input = sys.stdin.readline

n = int(input().strip())
sequence = [int(input().strip()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        
print('\n'.join(result)) if possible else print("NO")
    