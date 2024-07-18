t = int(input())

for i in range(t):
    string = input()
    score = 0
    result = 0
    for j in string:
        if j == 'O':
            score += 1
            result += score
        else:
            score = 0
    print(result)
            
    