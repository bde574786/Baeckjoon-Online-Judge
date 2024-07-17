numbers = []

for i in range(9):
    numbers.append(int(input()))

max_num = 0

for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        max_index = i

print(max_num)
print(max_index+1)