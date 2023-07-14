nums = list(map(int, input().split()))
target_number = int(input())

for i in range(len(nums)):
    if nums[i] == '':
        continue

    for j in range(i + 1, len(nums)):
        if nums[j] == '':
            continue

        if nums[i] + nums[j] == target_number:
            print(f"{nums[i]} + {nums[j]} = {target_number}")
            nums[j] = ''
            break
