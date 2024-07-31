import sys
input = sys.stdin.read
data = input().split()

k = int(data[0])
n = int(data[1])
lanes = list(map(int, data[2:]))

def count_lanes(length):
    return sum(lane // length for lane in lanes)

left, right = 1, max(lanes)
result = 0

while left <= right:                    
    mid = (left + right) // 2
    if count_lanes(mid) >= n:  
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)