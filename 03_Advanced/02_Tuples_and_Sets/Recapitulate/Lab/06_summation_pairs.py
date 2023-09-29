nums = list(map(int, input().split()))
target_number = int(input())

targets = []

for num in nums:
    if num in targets:
        print(f"{target_number - num} + {num} = {target_number}")
        targets.remove(num)
    else:
        target = target_number - num
        targets.append(target)
