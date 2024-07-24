n, k = map(int, input().split())
josephus = list(range(1, n+1))
result = []

idx = 0
while josephus:
    idx = (idx + k -1) % len(josephus)
    result.append(josephus.pop(idx))
    
print("<" + ", ".join(map(str, result)) + ">")
