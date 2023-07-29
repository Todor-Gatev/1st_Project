def func_executor(*args):
    return "\n".join(f"{func.__name__} - {func(*args_func)}" for func, args_func in args)
    # result = ""
    #
    # for func, args_func in args:
    #     result += f"{func.__name__} - {func(*args_func)}\n"
    #
    # return result


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor(
#     (sum_numbers, (1, 2)),
#     (multiply_numbers, (2, 4))
# ))
