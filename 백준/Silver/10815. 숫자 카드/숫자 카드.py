n = int(input())
cards = set(map(int, input().split()))

m = int(input())
given_cards = list(map(int, input().split()))

result = []
for i in given_cards:
    if i in cards:
        result.append(1)
    else:
        result.append(0)
        
print(" ".join(map(str, result)))