import sys
input = sys.stdin.readline
output = sys.stdout.write

t = int(input().rstrip())
results = []

for _ in range(t):
    a, b = map(int, input().rstrip().split())
    results.append(str(a + b))

output("\n".join(results) + "\n")
