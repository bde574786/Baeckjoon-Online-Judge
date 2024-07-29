import math

m, n = map(int, input().split())

def find_primes(m, n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    primes = [i for i in range(m, n  + 1) if is_prime[i]]
    return primes

for i in find_primes(m, n):
    print(i)