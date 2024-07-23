n = int(input())
peoples = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    peoples.append((age, name))

result = sorted(peoples, key=lambda x: x[0])

for i in result:
    print(i[0], i[1])