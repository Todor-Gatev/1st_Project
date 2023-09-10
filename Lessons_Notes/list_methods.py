# current_nums = nums.copy()!!!!! - if no copy is referent
lst = ['0', '1', '2', '9']
# a, *_, e = lst  # print(a, e) -> 0 9
a, *_, e = lst  # print(a, _, e) -> 0 ['1', '2'] 9

# bottles = list(map(int, input().split()))
# bottles = list(map(float, input().split()))
#
# if 0 <= idx < len(loot_items):
# if idx in range(len(loot_items)):

text = "0123456789"
# list_of_chars = list(text)
# print(list_of_chars)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(list_of_chars[:3])  # ['0', '1', '2']
# print(list_of_chars[-3:])  # ['7', '8', '9']
# print(list_of_chars[:-3])  # ['0', '1', '2', '3', '4', '5', '6']

idx, value = 5, 2
left_idx = idx - value
right_idx = idx + value
a_nums = list(text)
b_nums = list(text)
c_nums = list(text)
print(a_nums)
a_nums = a_nums[:left_idx] + a_nums[right_idx + 1:]
print(a_nums)
# =>
for i in range(idx + value, idx - value - 1, -1):
    b_nums.pop(i)
print(b_nums)
# =>
del c_nums[left_idx:right_idx + 1]
print(c_nums)

a = list(text)
a = list(filter(lambda x: x != '1', a))
print(a)

item_list = ['item', 5, 'foo', 3.14, True]
item_list = [e for e in item_list if e not in ('item', 5)]

item_list1 = ['item', 5, 'foo', 3.14, True]
list_to_remove = ['item', 5, 'foo']
final_list = list(set(item_list1) - set(list_to_remove))

# names = ['zorro', 'zz', 'apple', 'banana', 'cherry']
# sorted_names = sorted(names, key=lambda x: (-len(x), x))   # does not change the list
# print(sorted_names)   # ['banana', 'cherry', 'apple', 'zorro', 'zz']
# print(names)   # ['zorro', 'zz', 'apple', 'banana', 'cherry'] is not modified
# names = sorted(names, key=lambda x: (x, -len(x)))
# print(names)   # ['apple', 'banana', 'cherry', 'zorro', 'zz']
# names.sort()   # changes the list. Does not return result
# print(names)  # ['apple', 'banana', 'cherry', 'zorro', 'zz']

# command = "test 23 47"
# action, value = command.split(" ", 1)  # max 2 elements
# # action, value = command.split()  #
# print(action)  # test
# print(type(action))  # <class 'str'>
# print(value)  # 23 47
# print(type(value))  # <class 'str'>

# test = [1, 2, 3, 7, 4, 1]
# x = ("abc", 11, 12, 9)
# print(type(x))
# test.extend(x)
# print(test)
# print(set(test))

# print(', '.join(str(x) for x in test))
# print(*test, sep=', ')

fruits = ['apple', 'banana', 'cherry']
# x = fruits.pop(1)  # default idx=-1: last el
# print(fruits)  # ['apple', 'cherry']
# print(x)  # banana
# fruits.insert(12, "test1")  # inserts "test" at the end, because idx = 12 not in range
# fruits.insert(-11, "test2")  # inserts "test" at the beginning, because idx = -11 not in range
# fruits.insert(-2, "test3")
# print(fruits)

# x = [5, 10, 6, 3, 5, 4]
# x = [3]
# y = 4
# x[0] = x[-1]
# z = x.pop()
# x.insert(0, x[-1])
# print(x)

# def my_func(y):
#     if y < 18:
#         return False
#     else:
#         return True


# ages = [5, 12, 17, 18, 24, 32]
# adults = filter(lambda x: x > 17, ages)
# print(type(adults))
# print(adults)
# adults = list(filter(lambda x: x > 17, ages))
# print(type(adults))
# print(adults)
# adults2 = []
# for z in adults:
#     print(z)
#     print(type(z))
#     adults2.append(z)

# adults1 = [x for x in adults]
# adults2 = [x for x in ages]
# print(adults1)
# print(adults2)

# adults = [filter(lambda x: x > 17, ages)]
# adults = list(filter(lambda x: x > 17, ages))
# print(type(adults))
# print(adults)
# print(ages)

# test = [1, 2, 3, 1, 7, 4, 1]
# indexes = [idx for idx, el in enumerate(test) if el == 1]
# print(indexes)  # [0, 3, 6]
# indexes = [idx if el == 1 else print(el) for idx, el in enumerate(test)]
# print(indexes)  # [0, None, None, 3, None, None, 6]
# indexes = []
# while True:
#     try:
#         index = test_list.index('a')
#         indexes.append(index)
#         test_list[index] = None
#     except ValueError:
#         break
# print(indexes)  # [0, 3, 6]
