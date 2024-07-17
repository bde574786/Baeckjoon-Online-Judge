a = int(input())

for i in range(a):
    print(f"{' ' * (a-(i+1)) + '*' * (i+1)}")