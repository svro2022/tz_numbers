import random


def generate_expression(digits):
    operators = ['+', '-', '']
    expressions = [random.choice(operators) for _ in range(len(digits) - 1)]

    current_expression = ''.join([str(d) + op for d, op in zip(digits, expressions)]) + str(digits[-1])
    result = eval(current_expression)

    return current_expression, result


# Пример вызова функции
digits = list(range(9, -1, -1))
target_result = 200
num_variants = 5
found_variants = 0

# Попробуем генерировать выражения до тех пор, пока не найдем 5 подходящих вариантов
while found_variants < num_variants:
    expression, result = generate_expression(digits)
    if result == target_result:
        print(f"Выражение: {expression}, Результат: {result}")
        found_variants += 1
