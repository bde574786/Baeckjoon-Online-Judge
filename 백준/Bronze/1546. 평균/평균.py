n = int(input())
subject = list(map(int, input().split()))
m = max(subject)
result = []

for i in subject:
    result.append(i/m*100)

print(sum(result)/len(result))
