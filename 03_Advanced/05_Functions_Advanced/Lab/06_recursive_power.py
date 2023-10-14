# def recursive_power(num, power):  # short but not good for debugging
#     if power == 0:
#         return 1
#     return num * recursive_power(num, power - 1)

# def recursive_power(number, power):longer but in debug you can see how recursion works
#     result = 1
#     if power == 0:
#         return result
#     result = number * recursive_power(number, power - 1)
#     return result
#     # return number ** power
#
#
# print(recursive_power(2, 3))
# print(recursive_power(2, 0))
# # print(recursive_power(2, 10))
# # print(recursive_power(10, 100))

def a():  # infinite recursion
    a()


a()  # [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))
