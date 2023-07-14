def modify_list(f_num_list, num_f):
    for i in range(len(f_num_list)):
        if f_num_list[i] > num_f:
            f_num_list[i] -= num_f
        else:
            f_num_list[i] += num_f

    return f_num_list


# Read user input
nums = [int(x) for x in input().split()]

# Variables
summed_value_of_all_removed_elements = 0

# Logic
while nums:
    index = int(input())
    removed = 0

    if len(nums) == 1:
        removed = nums.pop()
    elif index < 0:
        removed = nums[0]
        nums[0] = nums[-1]
        # nums.insert(0, nums[-1])
        # removed = nums.pop(1)
    elif index > len(nums) - 1:
        removed = nums[-1]
        nums[-1] = nums[0]
        # nums.append(nums[0])
        # removed = nums.pop(-2)
    else:
        removed = nums.pop(index)

    nums = modify_list(nums, removed)
    summed_value_of_all_removed_elements += removed
# End of Logic

# Print Output
print(summed_value_of_all_removed_elements)
