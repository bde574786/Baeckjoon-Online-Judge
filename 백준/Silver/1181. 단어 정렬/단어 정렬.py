import sys

n = int(input())
strings = set(sys.stdin.readline().strip() for _ in range(n))

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

for i in sorted_strings:
    print(i)


