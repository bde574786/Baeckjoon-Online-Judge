a, b = input().split()

reversed_a = int(''.join(reversed(a)))
reversed_b = int(''.join(reversed(b)))

if reversed_a >= reversed_b:
    print(reversed_a)
else:
    print(reversed_b)