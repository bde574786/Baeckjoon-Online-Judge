# Divide and Conquer
def z(n, r, c):
    
    # base case
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    
    # 왼쪽 위
    if r < half and c < half:
        return z(n - 1, r, c)

    # 오른쪽 위
    elif r < half and c >= half:
        return half * half + z(n - 1, r, c - half)
    
    # 왼쪽 아래
    elif r >= half and c < half:
        return 2 * half * half + z(n - 1, r - half, c)
    
    # 오른쪽 아래
    else:
        return 3 * half * half + z(n - 1, r - half, c - half)

n, r, c = map(int, input().split())
print(z(n, r, c))
