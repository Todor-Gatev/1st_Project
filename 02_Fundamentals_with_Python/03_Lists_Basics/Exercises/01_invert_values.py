# Read user input
input_str_to_list = input().split()

# Variables
new_list = []
new_list_1 = []

# Logic
for char in input_str_to_list:
    new_list.append(-int(char))

# for i in range(len(input_str_to_list)):
#     # new_list[i] = -input_str_to_list[i]    # new_list do not have element with index i, because it's empty
#     # new_list.append(-input_str_to_list[i])  # new_list cannot append -string (minus string)
#     new_list_1.append(-int(input_str_to_list[i]))
# End of Logic

# Print Output
print(new_list)
# print(new_list_1)
