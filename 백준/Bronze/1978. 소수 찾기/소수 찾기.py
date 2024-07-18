n = int(input())
numbers = list(map(int, input().split()))
result = 0

for i in numbers:
    if i == 2:
        result += 1
    elif i > 2:
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result += 1

print(result)
