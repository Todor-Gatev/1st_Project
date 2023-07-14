nums = tuple(map(float, input().split()))
dict_nums = {}

for el in nums:
    dict_nums[el] = nums.count(el)

# for number, count in dict_nums.items():
#     print(f"{number} - {count} times")

[print(f"{number} - {count} times") for number, count in dict_nums.items()]
