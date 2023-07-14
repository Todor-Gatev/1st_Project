# from collections import OrderedDict  # can be used for ordered sets
# кортежи(tuple) и множества(set)
# b = (2) vs b = (2, )  !!!
# set can contain only immutable types (str, int, tuple....but not lists, sets..)
# my_tuple = {(1, 2, 3), [5, 6, 7, 1]}  # Error
# my_tuple = {(1, 2, 3), (5, 6, 7, 1)}  # OK
nums = [1, 2]
my_tuple = (nums, 7, 9)  # tuple are immutable but variables are mutable
print(my_tuple)  # ([1, 2], 7, 9)
nums.append(3)  # change NUMS in tuple!!!
# nums = [1, 2, 3]  # does not change NUMS in tuple!!!
print(my_tuple)  # ([1, 2, 3], 7, 9) -> variables inside the tuple are mutable
my_tuple[0][2] = 12
print(my_tuple)  # ([1, 2, 12], 7, 9) -> variables inside the tuple are mutable

# my_tuple = (1, 2, 3) <=> 1, 2, 3
# my_tuple = 1, 2, 3 <=> (1, 2, 3)

#
# test_tuple = (1, 2, 3, 1, 7, 4, 1)
# indexes = [idx for idx, el in enumerate(test_tuple) if el == 1]
# print(indexes)  # [0, 3, 6]
# indexes = [idx if el == 1 else print(el) for idx, el in enumerate(test_tuple)]
# print(indexes)  # [0, None, None, 3, None, None, 6]

# my_set = set()

my_set = {"apple", "banana", "cherry"}
my_set.discard("test")  # does not raise error if el not in set
print(my_set)  # {'apple', 'banana', 'cherry'}
my_set.remove("test")  # KeyError: 'test'
my_set.discard("banana")
print(my_set)  # {'cherry', 'apple'}
