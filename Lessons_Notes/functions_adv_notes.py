# # recursion is time and space consuming - can be used when there is dictionary in dictionary...unknown times
# # recursion - see lab task 6 and recursive_funcs.py
#
# def sum_nums(a, c=5,  *args):  # *args (packing)-> tuple with 0 or more ele-> a: 3 c: 7 args: (12, 19)
#     res = a + c
#     for num in args:
#         res += num
#     return res
#
#
# z = [1, 2, 3]
# sum_nums(3, 7, *z)
# sum_nums(3, 7, 12, 19)
#
#
def test_kwargs(a, **kwargs):  # **kwargs -> dict with 0 or more ele-> a: 3  kwargs: {'b': 7, 'c': 12}
    print(a)
    print(kwargs)

my_dic = {'b': 7, 'c': 12}
test_kwargs(3, **my_dic)
test_kwargs(3, b=7, c=12)
test_kwargs(a=3)
#
# print(**{"name": "George", "town": "Sofia", "age": 20})  # error
# print(*[1, 2, 3])  # OK
#
#
# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))  # **(unpacking) transforms dict to next row
# print(get_info(name="George", town="Sofia", age=20))  # kwargs can read this tipe of info
# print(get_info("George", "Sofia", 20))  # for correct result needs correct sequence

# def a(x1, y1):
#     x = 'xa'  # not changed on global scope
#     print(x)  # xa  => changed on local scope
#     print(x1)  # x  => not changed on global scope
#
#     def b():
#         global y  # y  => changed on global scope
#         nonlocal y1
#         y1 = 'y1b'
#         y = 'yb'
#         print(y)  # yb  => changed on global scope
#         print(y1)  # y1b  => changed on local scope
#
#     return b  # if not return b -> b is hidden
#
#
# x = 'x'
# y = 'y'
# a(x, y)()  # if b is not hidden, we can indirectly call b
# # res = a(x, y)
# # res()  # if b is not hidden, we can indirectly call b
# print(x)
# print(y)
# # # b()  # ERROR


# region Function Returning Function Example
def calculator(operator):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction


operation = calculator("+")
result = operation(2, 3)
print(result)

# endregion


# def factorial(number):
#     if not isinstance(number, int) or number < 0:
#         return f"Sorry. 'number' is incorrect."
#
#     def inner_factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact = fact * i
#         return fact
#
#     return inner_factorial(number)
#
#
# print(factorial(5))  # 120
# print(factorial(-5))  # Sorry. 'number' is incorrect.
# print(factorial('a'))  # Sorry. 'number' is incorrect.

# def not_recursion():
#     def not_recursion():
#         def not_recursion():
#             print(3)
#
#         print(2)
#         not_recursion()
#
#     print(1)
#     not_recursion()
#
# not_recursion()
