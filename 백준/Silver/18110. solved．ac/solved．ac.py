import sys

def my_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

input = sys.stdin.readline
n = int(input())

if n != 0:
    level = [int(input()) for _ in range(n)]
    remove_level = my_round(n * 0.15)
    result = sorted(level)[remove_level: n - remove_level]
    average = my_round(sum(result)/len(result))
    print(average)
else:
    print(0)

