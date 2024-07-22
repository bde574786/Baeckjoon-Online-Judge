import sys

strings = [sys.stdin.readline().strip() for _ in range(3)]
value = [int(v) + (3 - i) for i, v in enumerate(strings) if v.isnumeric()][0]

if value % 15 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")

else:
    print(value)