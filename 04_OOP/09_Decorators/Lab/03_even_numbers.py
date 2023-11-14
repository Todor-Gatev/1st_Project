# def even_numbers(function):
#     def wrapper(*args, **kwargs):
#         return [n for n in function(*args, **kwargs) if n % 2 == 0]
#
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
#
# print(get_numbers([1, 2, 3, 4, 5]))

def even_numbers(function):
    def wrapper(*args, **kwargs):
        return [n for list_i in function(*args, **kwargs) for n in list_i if n % 2 == 0]

    return wrapper


# @even_numbers
# def get_numbers(n1, n2):
#     return n1, n2
#
#
# # x1 = [1, 2, 3, 4, 5]
# # x2 = [6, 7, 8]
# # print(get_numbers(x1, x2))
#
# print(get_numbers([1, 2, 3, 4, 5], [6, 7, 8]))

@even_numbers
def get_numbers(n1):
    return n1


# print(get_numbers([1, 2, 3, 4, 5]))  # Error
print(get_numbers([[1, 2, 3, 4, 5]]))  # [2, 4]
