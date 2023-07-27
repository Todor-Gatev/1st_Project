def recursive_power(number, power):
    result = 1
    if power == 0:
        return result
    result = number * recursive_power(number, power - 1)
    return result
    # return number ** power

# def recursive_power(number, power):
#     if power == 1:
#         return number
#     return number * recursive_power(number, power - 1)
#     # return number ** power


print(recursive_power(2, 3))
print(recursive_power(2, 0))
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))

# def a():
#     a()
#
#
# a()

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
