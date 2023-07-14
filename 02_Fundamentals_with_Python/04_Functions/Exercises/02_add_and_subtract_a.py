def sum_numbers(num1, num2):
    return num1 + num2


def subtract_test(sum_num12, num3):
    return sum_num12 - num3


def add_and_subtract(a, b, c):
    result = subtract_test(sum_numbers(a, b), c)
    return result


# Read user input
x = int(input())
y = int(input())
z = int(input())

# Print Output
print(add_and_subtract(x, y, z))
