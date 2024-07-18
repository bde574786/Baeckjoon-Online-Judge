n = int(input())
size = list(map(int,input().split()))
t,p = map(int,input().split())

shirts = 0
for i in range(len(size)):
    if size[i]%t == 0:
        shirts += int(size[i]/t)
    else:
        shirts += (int(size[i]/t)+1)

print(shirts)

pen = [int(n/p), n%p]
print(*pen)