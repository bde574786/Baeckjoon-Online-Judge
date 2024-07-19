n = int(input())
result = []

for i in range(1, n):
    digit_sum = sum(map(int, str(i)))
    if i + digit_sum == n:
        result.append(i)
        
if len(result) != 0:
    print(min(result))
else:
    print(0)