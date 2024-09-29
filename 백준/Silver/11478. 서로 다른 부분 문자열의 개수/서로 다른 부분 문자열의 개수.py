strings = input()
substrings = set()

for i in range(len(strings)):
    for j in range(i + 1, len(strings) + 1):
        substrings.add(strings[i:j])

print(len(substrings))