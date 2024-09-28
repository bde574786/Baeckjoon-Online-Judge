n = int(input())

in_office = set()

for _ in range(n):
    name, action = input().split()

    if action == "enter":
        in_office.add(name)
    else:
        in_office.remove(name)

people = sorted(in_office, reverse=True)

for i in people:
    print(i)