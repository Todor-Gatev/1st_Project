# Read user input
input_list = input().split()
command = input()

# Variables

# Logic
while command != "3:1":
    new_list = []
    action, index, end_info = command.split()
    index = int(index)

    if index > len(input_list) - 1:
        command = input()
        continue

    if action == "merge":
        end_index = int(end_info)
        new_str = ""
        for i in range(len(input_list)):
            if i < index or i > end_index:
                new_list.append(input_list[i])
            else:
                if i == min(end_index, (len(input_list) - 1)):
                    new_str += input_list[i]
                    new_list.append(new_str)
                else:
                    new_str += input_list[i]
    elif action == "divide":
        partitions = int(end_info)

        for i in range(len(input_list)):
            if i != index:
                new_list.append(input_list[i])
            else:
                str_ing = input_list[i]
                substrings_length = len(str_ing) // partitions
                for j in range(partitions):
                    sub_str_start = j * substrings_length
                    sub_str_end = sub_str_start + substrings_length
                    if j < partitions - 1:
                        new_list.append(str_ing[sub_str_start:sub_str_end])
                    else:
                        new_list.append(str_ing[sub_str_start:])

    input_list = new_list
    command = input()
# End of Logic

# Print Output
print(" ".join(input_list))
