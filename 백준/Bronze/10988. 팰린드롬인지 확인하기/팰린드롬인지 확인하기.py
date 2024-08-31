word = input()
print(1 if word==''.join(reversed(word)) else 0)