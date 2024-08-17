submitted = set()

for _ in range(28):
    n = int(input())
    submitted.add(n)

all_students = set(range(1, 31))
result = sorted(all_students - submitted)

print(result[0])
print(result[1])
