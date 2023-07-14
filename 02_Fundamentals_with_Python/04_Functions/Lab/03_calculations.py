def calcs(operators, a, b):
    result = None
    if operators == "multiply":
        result = a + b
    elif operators == "divide":
        result = a // b
    elif operators == "add":
        result = a + b
    elif operators == "subtract":
        result = a - b

    return result


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calcs(input_operator, first_num, second_num))
