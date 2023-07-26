# def sum_nums(a, c=5,  *args):  # *args (packing)-> tuple with 0 or more ele-> a: 3 c: 7 args: (12, 19)
#     res = a + c
#     for num in args:
#         res += num
#     return res

# def sum_values(a, **kwargs):  # **kwargs -> dict with 0 or more ele-> a: 3  kwargs: {'b': 7, 'c': 12}
#     return kwargs


# z = [1, 2, 3]
# sum_nums(3, 7, *z)
# sum_nums(3, 7, 12, 19)
# sum_values(3, b=7, c=12)
# sum_values(a=3)

# print(**{"name": "George", "town": "Sofia", "age": 20})  # error
# print(*[1, 2, 3])  # OK

# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))  # **(unpacking) transforms dict to next row
# print(get_info(name="George", town="Sofia", age=20))  # kwargs can read this tipe of info
# print(get_info("George", "Sofia", 20))  # for correct result needs correct sequence
