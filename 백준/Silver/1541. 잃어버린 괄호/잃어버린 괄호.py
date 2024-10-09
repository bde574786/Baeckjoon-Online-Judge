def minimize_expression(expression):
    parts = expression.split('-')

    first_part_sum  = sum(map(int, parts[0].split('+')))

    other_sum = 0
    for part in parts[1:]:
        numbers = part.split('+')
        part_sum = 0
        for number in numbers:
            part_sum += int(number)
        other_sum += part_sum

    return first_part_sum  - other_sum

expression = input()
print(minimize_expression(expression))
