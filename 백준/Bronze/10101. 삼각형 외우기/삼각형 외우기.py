angles = []
for _ in range(3):
    angle = int(input())
    angles.append(angle)

if sum(angles) != 180:
    print("Error")
elif angles.count(angles[0]) == 3:
    print("Equilateral")
elif len(set(angles)) == 2:
    print("Isosceles")
elif len(set(angles)) == 3:
    print("Scalene")