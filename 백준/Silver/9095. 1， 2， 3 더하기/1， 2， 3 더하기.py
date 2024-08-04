t = int(input())
test_cases = [int(input()) for _ in range(t)]

ways = [0] * 11
ways[1] = 1
ways[2] = 2
ways[3] = 4

for i in range(4, 11):
    ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

for n in test_cases:
    print(ways[n])
