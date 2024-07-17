n = int(input())
num_list = list(map(int, input().split()))

max_num = num_list[0]
min_num = num_list[0]

for i in range(len(num_list)):
    if num_list[i] > max_num:
        max_num = num_list[i]
    if num_list[i] < min_num:
        min_num = num_list[i]
        
print(min_num, max_num, sep=' ')