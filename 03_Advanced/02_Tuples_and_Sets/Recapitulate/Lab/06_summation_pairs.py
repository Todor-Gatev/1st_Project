nums = tuple(int(x) for x in input().split())
target = int(input())

needed_nums = []

for el in nums:
    if el in needed_nums:
        print(f"{target - el} + {el} = {target}")
        needed_nums.remove(el)
    else:
        needed_nums.append(target - el)


# nums = list(map(int, input().split()))
# target_number = int(input())
#
# targets = []
#
# for num in nums:
#     if num in targets:
#         print(f"{target_number - num} + {num} = {target_number}")
#         targets.remove(num)
#     else:
#         target = target_number - num
#         targets.append(target)
