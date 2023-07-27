from functools import reduce


def operate(operator, *args):
    map_functions = {
        '*': lambda x: reduce(lambda a, b: a * b, x),
        '/': lambda x: reduce(lambda a, b: a / b, x),
        '+': lambda x: reduce(lambda a, b: a + b, x),
        '-': lambda x: reduce(lambda a, b: a - b, x),
    }

    return map_functions[operator](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("*", 3))
print(operate("/", 3))
print(operate("-", 3))
