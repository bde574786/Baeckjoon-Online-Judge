n = int(input())
string = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
result = 0

for i in range(len(string)):
    char = alpha.find(string[i]) + 1
    result += char*(31**i)

print(result)