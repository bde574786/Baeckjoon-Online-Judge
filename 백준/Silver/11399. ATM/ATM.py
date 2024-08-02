import sys

input = sys.stdin.readline
n = int(input().strip())
time = list(map(int, input().strip().split()))

time.sort()

total_time = 0
current_time = 0
for i in time:
    current_time += i
    total_time += current_time
    
print(total_time)