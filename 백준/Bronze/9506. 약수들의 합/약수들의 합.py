import sys

input = sys.stdin.readline

while True:
    factors = []
    n = int(input())
        
    if n == -1:
        break
    
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        print(f"{n} = {' + '.join(map(str, factors))}")
    else:
        print(f"{n} is NOT perfect.")
