import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

not_heard = set()
not_seen = set()

for _ in range(n):
    name = input().strip()
    not_heard.add(name)

for _ in range(m):
    name = input().strip()
    not_seen.add(name)
    
result = not_heard & not_seen

print(len(result))
for _ in sorted(result):
    print(_)