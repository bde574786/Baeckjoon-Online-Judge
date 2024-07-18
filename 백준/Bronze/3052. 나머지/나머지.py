result_set = set()

for _ in range(10):
    number = int(input())
    remainder = number%42
    result_set.add(remainder)
    
print(len(result_set))
    
    