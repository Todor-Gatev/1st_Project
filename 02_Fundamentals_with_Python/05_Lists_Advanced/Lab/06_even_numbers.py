# Read user input
nums_list = [int(x) for x in input().split(", ")]

# Variables

# Logic
# even_nums_index_list = []
even_nums_index_list = [x for x in range(len(nums_list)) if nums_list[x] % 2 == 0]

# for i in range(len(nums_list)):
#     if nums_list[i] % 2 == 0:
#         even_nums_index_list.append(i)
# End of Logic

# Print Output
print(even_nums_index_list)
