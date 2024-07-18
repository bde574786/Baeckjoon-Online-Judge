t = int(input())

for i in range(t):
    number, string = input().split()
    result = ''
    for j in string:
        result += int(number)*j
    print(result)