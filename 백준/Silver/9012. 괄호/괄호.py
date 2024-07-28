t = int(input())

for i in range(t):
    stack = []
    string = input()
    result = "YES"
    
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                result = "NO"
                break
            stack.pop()

    if stack:
        result = "NO"

    print(result)