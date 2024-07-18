while(True):
    num_list = list(map(int, input().split()))
    if sum(num_list) == 0:
        break
    
    max_num = max(num_list)
    num_list.remove(max_num)
    if num_list[0]**2 + num_list[1]**2 == max_num**2:
        print("right")
    else:
        print("wrong")