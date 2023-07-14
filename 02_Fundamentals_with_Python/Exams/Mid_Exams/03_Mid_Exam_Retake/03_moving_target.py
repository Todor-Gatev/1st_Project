# Read user input
targets = [int(x) for x in input().split()]
command = input()

# Variables

# Logic
while command != "End":
    action, idx, value = command.split()
    idx = int(idx)
    value = int(value)
    is_valid_idx = 0 <= idx < len(targets)

    if action == "Shoot":
        if is_valid_idx:
            targets[idx] -= value
            if targets[idx] <= 0:
                targets.pop(idx)
    elif action == "Add":
        if is_valid_idx:
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= idx - value and idx + value < len(targets):
            targets = targets[:(idx - value)] + targets[(idx + value + 1):]
            # for i in range(idx + value, idx - value - 1, -1):
            #     targets.pop(i)
        else:
            print("Strike missed!")

    command = input()
# End of Logic

# Print Output
print(*targets, sep='|')
