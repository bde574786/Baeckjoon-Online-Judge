import sys

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
min_height = min(map(min, land))
max_height = max(map(max, land))
result = sys.maxsize
result_height = 0

# Brute Force
for height in range(min_height, max_height + 1):
    remove_blocks, add_blocks = 0, 0

    for i in range(n):
        for j in range(m):
            if land[i][j] > height:
                remove_blocks += land[i][j] - height 
            else:
                add_blocks += height - land[i][j]

    if remove_blocks + b >= add_blocks:
        time = remove_blocks * 2 + add_blocks

        if time <= result:
            result = time
            result_height = height

print(result, result_height)