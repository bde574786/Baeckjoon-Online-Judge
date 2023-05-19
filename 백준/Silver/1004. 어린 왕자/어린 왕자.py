T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planetNumber = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start = ((x1-cx)**2 + (y1-cy)**2)**0.5 # 행성의 중심부터 시작점까지의 거리
        end = ((x2-cx)**2 + (y2-cy)**2)**0.5 # 행성의 중심부터 도착점까지의 거리
        
        if start < r and end < r: # 시작점과 도착점 모두 원 안에 있는 경우
            pass
        elif start < r: # 시작점은 원 안에 도착점은 원 밖에 있는 경우
            planetNumber += 1
        elif end < r: # 도착점은 원 안에 시작점은 원 밖에 있는 경우
            planetNumber += 1
        
        
    print(planetNumber)