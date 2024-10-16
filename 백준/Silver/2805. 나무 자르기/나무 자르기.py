import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)        

# Binary Search    
while low <= high:
    mid = (low + high) // 2

    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    
    if total >= m:
        low = mid + 1
    else:
        high = mid - 1
        
print(high)
