# Read user input
presents_list = input().split()
command = input()

# Variables

# Logic
while command != "No Money":
    if not presents_list:
        break
    command = command.split()

    if command[0] == "OutOfStock":
        for i in range(len(presents_list)):
            if presents_list[i] == command[1]:
                presents_list[i] = "None"
    elif command[0] == "Required":
        if 0 <= float(command[2]) < len(presents_list):
            presents_list[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        presents_list[-1] = command[1]

    command = input()
# End of Logic

# Print Output
print(' '.join(x for x in presents_list if x != "None"))
