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

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)  # default idx=-1: last el
print(fruits)  # ['apple', 'cherry']
print(x)  # banana
fruits.insert(12, "test1")
fruits.insert(-11, "test2")
fruits.insert(-2, "test3")
print(fruits)

