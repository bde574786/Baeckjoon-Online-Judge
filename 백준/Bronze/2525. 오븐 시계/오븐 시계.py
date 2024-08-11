a, b = map(int, input().split())
c = int(input())

total_minutes = a * 60 + b + c

hours = (total_minutes // 60) % 24
minutes = total_minutes % 60

print(hours, minutes)
