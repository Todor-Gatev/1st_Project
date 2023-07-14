def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    return factorial


def do_divide(a, b):
    return get_factorial(a) / get_factorial(b)


num_1 = int(input())
num_2 = int(input())

print(f"{do_divide(num_1, num_2):.2f}")
