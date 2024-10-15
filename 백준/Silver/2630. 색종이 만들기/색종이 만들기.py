# Quad Tree
def count_paper(x, y, n):
    global white, blue
    color = paper[x][y]
    same_color = True
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                same_color = False
                break
        if not same_color:
            break
        
    if same_color:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        count_paper(x, y, half)
        count_paper(x, y + half, half)
        count_paper(x + half, y, half)
        count_paper(x + half, y + half, half)
    
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

count_paper(0, 0, n)

print(white, blue, sep='\n')