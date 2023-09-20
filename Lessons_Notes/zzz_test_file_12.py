from sys import path
print(*path, sep="\n")

# my_list = ['a', 'b', 'c', 'd']
# a = ' - '.join(x for x in my_list)
# print(a)
# b = '\n'.join([f"- {x}" for x in my_list])
# [print(f" - {x}") for x in my_list]
# print(b)

# my_list = [1, 2, 3, 1, 2, 2,  2, 2, 4, 5, 'a']
# result = list(filter(lambda x: x == 2, my_list))  # [2, 2, 2, 2, 2]
# result1 = next(filter(lambda x: x == 2, my_list))  # 2
# result2 = next(filter(lambda x: x == 7, my_list), "Not in list")  # Not in list
# # result3 = next(filter(lambda x: x == 7, my_list))  # StopIteration (error)
#
# print(result)
# print(result1)
# print(result2)
# # print(result3)

# class Product:
#     def __init__(self, name: str, price: float):
#         self.__name = name
#         self.__price = price
#
#     # region getters
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def price(self):
#         return self.__price
#     # endregion
#
#
# p = Product("asd", 3)
# print(p.name)
#
# p.__name = "fff"
# print(p.name)
# p._Product__name = "fff"
# print(p.name)
#
# p.ass = "ass"
# print(p.ass)
# p.name = "blabla"


# print(int("asd"))  # ValueError: invalid literal for int() with base 10: 'asd'
# print(int("2"))  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

# fruits = ['apple', 'banana', 'cherry']
#
# points = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# fruits.extend(points)
#
# print(fruits)

a = [[]] * 3
print(a)
