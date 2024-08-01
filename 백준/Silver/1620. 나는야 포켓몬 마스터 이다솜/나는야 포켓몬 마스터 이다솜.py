import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

pokemon_to_num = {}
num_to_pokemon = [""] * (n + 1)

for i in range(1, n + 1):
    name = input().strip()
    pokemon_to_num[name] = i
    num_to_pokemon[i] = name

for _ in range(m):
    query = input().strip()
    if query.isdigit():
        num = int(query)
        print(num_to_pokemon[num])
    else:
        print(pokemon_to_num[query])