nums = tuple(map(float, input().split()))
dict_nums = {}

for el in nums:
    if el not in dict_nums:
        dict_nums[el] = 0

    dict_nums[el] += 1

# for number, count in dict_nums.items():
#     print(f"{number} - {count} times")

[print(f"{number} - {count} times") for number, count in dict_nums.items()]
