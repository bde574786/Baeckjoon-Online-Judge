n = int(input())
words = []

for _ in range(n):
    word = input()
    words.append(word)

count = 0
for word in words:
    seen = set()
    is_group_word = True
    prev_char = ''
    
    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        count += 1

print(count)