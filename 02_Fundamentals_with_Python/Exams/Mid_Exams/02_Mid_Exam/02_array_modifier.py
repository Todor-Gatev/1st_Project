# Read user input
int_list = [int(x) for x in input().split()]
command = input()

# Variables

# Logic
while command != "end":
    el_command = command.split()

    if el_command[0] == "swap":
        index1 = int(el_command[1])
        index2 = int(el_command[2])
        int_list[index1], int_list[index2] = int_list[index2], int_list[index1]
    elif el_command[0] == "multiply":
        index1 = int(el_command[1])
        index2 = int(el_command[2])
        product = int_list[index1] * int_list[index2]
        int_list[index1] = product
    elif el_command[0] == "decrease":
        int_list = [(x-1) for x in int_list]

    command = input()

str_list = [str(x) for x in int_list]
# End of Logic

# Print Output
print(', '.join(str_list))
