import sys
from collections import Counter

input = sys.stdin.readline
n = int(input().strip())
numbers = []

for _ in range(n):
    numbers.append(int(input().strip()))

sorted_numbers = sorted(numbers)

print(round(sum(numbers)/len(numbers)))
print(sorted_numbers[len(numbers)//2])

counter = Counter(numbers)
max_frequency = max(counter.values())
mode = [key for key, value in counter.items() if value == max_frequency]
sorted_mode = sorted(mode)

if len(sorted_mode) > 1:
    print(sorted_mode[1])
else:
    print(sorted_mode[0])

print(max(numbers)-min(numbers))