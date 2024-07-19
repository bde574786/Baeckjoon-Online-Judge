while(True):
    number = input()
    reversed_number = ''
    if number == '0':
        break
    for i in reversed(range(len(number))):
        reversed_number += number[i]
    
    if number == reversed_number:
        print("yes")
    else:
        print("no")