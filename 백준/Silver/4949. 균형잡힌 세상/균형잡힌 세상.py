brackets = {')': '(', ']': '['}

while True:
  stack = []
  balanced = True
  string = input()
  if string == '.':
    break
  for i in string:
    if i in brackets.values():
      stack.append(i)
    elif i in brackets.keys():
      if not stack or stack.pop() != brackets[i]:
        balanced = False
        break
  
  if stack:
    balanced = False
  
  if balanced:
    print("yes")
  else:
    print("no")