def find_prime_sum_and_min(m, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(m, n + 1) if is_prime(i)]
    
    if primes:
        prime_sum = sum(primes)
        prime_min = min(primes)
        print(prime_sum)
        print(prime_min)
    else:
        print(-1)
    
m = int(input())
n = int(input())

find_prime_sum_and_min(m, n)