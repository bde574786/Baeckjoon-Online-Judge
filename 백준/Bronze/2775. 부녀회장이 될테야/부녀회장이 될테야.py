def caculate_people(k, n):
    apt = [[i for i in range(n+1)]]

    for i in range(1, k+1):
        floor = [0] * (n+1)

        for j in range(1, n+1):
            floor[j] = floor[j-1] + apt[i-1][j]
        apt.append(floor)
        
    return apt[k][n]

t = int(input())

for i in range(1, t+1):
    n = int(input())
    k = int(input())
    print(caculate_people(n, k))

