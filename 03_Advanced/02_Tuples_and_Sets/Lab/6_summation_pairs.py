nums = list(map(int, input().split()))
target_number = int(input())

targets = set()
values_map = {}

for num in nums:
    if num in targets:
        print(f"{values_map[num]} + {num} = {target_number}")
        targets.remove(num)
        del values_map[num]
    else:
        target = target_number - num
        targets.add(target)
        values_map[target] = num

# targets = set()
# values_map = {}

# for num in nums:
#     if num in targets:
#         print(f"{values_map[num]} + {num} = {target_number}")
#         targets.remove(num)
#         del values_map[num]
#     else:
#         target = target_number - num
#         targets.add(target)
#         values_map[target] = num
