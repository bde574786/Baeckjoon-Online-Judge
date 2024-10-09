import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
result = []

for _ in range(n):
    number = int(input())
    
    if number > 0:
        heapq.heappush(heap, number)
    elif number == 0:
        if heap:
            result.append(str(heapq.heappop(heap)))
        else:
            result.append('0')
    
sys.stdout.write("\n".join(result) + "\n")