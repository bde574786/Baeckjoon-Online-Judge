n = int(input())

for _ in range(n):   
    a, b = map(int, input().split())
    print(f"Case #{_ + 1}: {a} + {b} = {a + b}")
