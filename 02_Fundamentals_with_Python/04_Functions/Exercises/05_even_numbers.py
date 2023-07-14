# def is_even_digit(digit):
#     return digit % 2 == 0
#

nums = [int(x) for x in input().split()]
print(list(filter(lambda x: x % 2 == 0, nums)))
# print(list(filter(is_even_digit, nums)))

# y = (filter(lambda x: x % 2 == 0, nums))
# print(list(filter(lambda x: x % 2 != 0, nums)))
# print(nums)
# print(x)
