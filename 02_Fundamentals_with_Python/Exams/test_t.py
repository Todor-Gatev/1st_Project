# class MyClass:
#     """This is MyClass."""
#
#     def example(self):
#         """This is the example module of MyClass."""
#
#
# print(MyClass.__doc__)  # This is MyClass.
# print(MyClass.example.__doc__)
# # This is the example module of MyClass.


# my_list = [7, 1, 1, 13, 1, 2, 2, 1, 4, 3, 1]
# for num in my_list:
#     if num == 1:
#         my_list.remove(num)
#
# print(my_list)

# fruits = ['apple', 'banana', 'cherry']
# x = fruits.pop(1)  # default idx=-1: last el
# print(fruits)  # ['apple', 'cherry']
# print(x)  # banana
# fruits.insert(12, "test1")
# fruits.insert(-11, "test2")
# fruits.insert(-2, "test3")
# print(fruits)

# my_list = [1, 2, 3, 1, 4, 5, 'a']
# result = list(filter(lambda x: x == 1, my_list))  # [1, 1]
# result1 = next(filter(lambda x: x == 1, my_list))  # 1
# result2 = next(filter(lambda x: x == 7, my_list), "Not in list")  # Not in list
# result3 = next(filter(lambda x: x == 7, my_list))  # StopIteration (error)
#
# print(result)
# print(result1)
# print(result2)

from sys import path
print(*path, sep="\n")

# a = f"{'-' * 11}\n{'-' * 11}"
# print(a)

# date = "20.3.2223"
# date = date.split('.')
# print(date[1])
# print(type(date[1]))
# num_month = {"01": "January", "2": "February", "3": "March", "4": "April", "5": "May"}
# print(num_month[date[1]])

# print(isinstance('a', int))  # False
# print(isinstance(5, int))  # True

a = "12345"
b = list(a)  # ['1', '2', '3', '4', '5']
print(b)
