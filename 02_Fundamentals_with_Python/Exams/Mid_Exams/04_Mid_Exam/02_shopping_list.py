# Read user input
items = input().split('!')
command = input()

# Variables

# Logic
while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]

    if action == "Urgent":
        if item in items:
            command = input()
            continue
        items.insert(0, item)
    elif action == "Unnecessary":
        if item in items:
            items.remove(item)
    elif action == "Correct":
        if item in items:
            new_item = command[2]
            item_idx = items.index(item)
            items[item_idx] = new_item
    elif action == "Rearrange":
        if item in items:
            items.remove(item)
            items.append(item)
    command = input()
# End of Logic

# Print Output
print(*items, sep=', ')
