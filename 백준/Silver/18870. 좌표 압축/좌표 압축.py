n = int(input())
coordinates = list(map(int, input().split()))
sorted_coordinates = sorted(set(coordinates))

map_coordinates = {value: idx for idx, value in enumerate(sorted_coordinates)}

result = [map_coordinates[x] for x in coordinates]
print(" ".join(map(str, result)))
