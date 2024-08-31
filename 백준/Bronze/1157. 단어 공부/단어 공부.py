from collections import Counter

word = input()
word = word.upper()
count = Counter(word)
max_count = max(count.values())
most_common = [k for k, v in count.items() if v == max_count]

if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])