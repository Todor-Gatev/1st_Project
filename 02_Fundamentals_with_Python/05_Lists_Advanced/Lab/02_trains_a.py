# Read user input
wagons = int(input())

# Variables
train_list = [0] * wagons
command = "add 0"

# Logic
while command != "End":
    command_elements = command.split()

    if command_elements[0] == "add":
        train_list[-1] += int(command_elements[1])
    elif command_elements[0] == "insert":
        train_list[int(command_elements[1])] += int(command_elements[2])
    elif command_elements[0] == "leave":
        train_list[int(command_elements[1])] -= int(command_elements[2])

    command = input()
# End of Logic

# Print Output
print(train_list)
