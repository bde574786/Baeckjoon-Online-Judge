"""
문제에서는 과일을 앞에서 몇 개, 뒤에서 몇 개를 뺀다고 설명하지만, 
알고리즘적으로는 전체 과일 배열을 탐색하면서 두 종류 이하의 과일로 구성된 
가장 긴 연속 구간을 찾는 방식이다.
"""

n = int(input())
fruits = list(map(int, input().split()))

result_max = 0
start = 0
fruit_count = {}

for end in range(n):
    # 딕셔너리에 과일 개수 저장
    fruit = fruits[end]
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
    
    # 종류가 두 종류가 넘어가면 시작 포인터를 옮김
    while len(fruit_count) > 2:
        left_fruit = fruits[start]
        fruit_count[left_fruit] -= 1
        if fruit_count[left_fruit] == 0:
            del fruit_count[left_fruit]
            
        start += 1
    
    result_max = max(result_max, end - start + 1)

print(result_max)