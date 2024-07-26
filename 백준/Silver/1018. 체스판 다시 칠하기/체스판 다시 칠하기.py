n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
result = []
min_repaints = 64

for i in range(n-7):
    for j in range(m-7):
        repaints_w = 0
        repaints_b = 0
        
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[i + x][j + y] != 'W':
                        repaints_w += 1
                    if board[i + x][j + y] != 'B':
                        repaints_b += 1
                else:
                    if board[i + x][j + y] != 'B':
                        repaints_w += 1
                    if board[i + x][j + y] != 'W':
                        repaints_b += 1
        
        min_repaints = min(min_repaints, repaints_w, repaints_b)

print(min_repaints)