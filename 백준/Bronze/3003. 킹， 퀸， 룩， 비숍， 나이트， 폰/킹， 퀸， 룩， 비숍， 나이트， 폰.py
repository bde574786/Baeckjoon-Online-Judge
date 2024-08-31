pieces = [1, 1, 2, 2, 2, 8]
found_pieces = list(map(int, input().split()))

result = [pieces[i] - found_pieces[i] for i in range(6)]
for i in result:
    print(i, end=' ')
