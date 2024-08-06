def padovan_sequence(n):
    padovan = [1, 1, 1]
    
    for i in range(3, n):
        padovan.append(padovan[i-2] + padovan[i-3])

    return padovan

t = int(input())
test_cases = [int(input()) for _ in range(t)]
max_n = max(test_cases)

padovan = padovan_sequence(max_n)

for n in test_cases:
    print(padovan[n-1])
