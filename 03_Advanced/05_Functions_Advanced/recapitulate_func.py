from functools import reduce


def operate(operator, *args):
    map_func = {
        '+': lambda x: reduce(lambda a, b: a + b, args),
        '-': lambda x: reduce(lambda a, b: a - b, args),
        '*': lambda x: reduce(lambda a, b: a * b, args),
        '/': lambda x: reduce(lambda a, b: a / b, args),
    }
    return map_func[operator](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
