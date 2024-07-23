import sys

n = int(input())
num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

for i in sorted(num_list):
    print(i)