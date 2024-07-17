num_list = []

for i in range(3):
    number = int(input())
    num_list.append(number)
    
multiply_num = num_list[0] * num_list[1] * num_list[2]
result = [0 for _ in range(10)]

for i in str(multiply_num):
    result[int(i)] += 1

for i in result:
    print(i)