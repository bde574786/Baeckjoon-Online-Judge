import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    numbers = [True] * (2*n + 1)
    numbers[0] = numbers[1] = False
    
    for i in range(2, int(2*n **0.5) + 1):
        if numbers[i]:
            for j in range(i * i, 2*n + 1, i):
                numbers[j] = False
    
    count = 0
    for i in range(n + 1, 2*n + 1):
        if numbers[i]:
            count += 1
        
    print(count)
