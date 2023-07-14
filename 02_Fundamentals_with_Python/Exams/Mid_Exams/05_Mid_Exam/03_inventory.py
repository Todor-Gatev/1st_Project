# Read user input
items = input().split(", ")
command = input()

# Variables

# Logic
while command != "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        if item in items:
            pass
        else:
            items.append(item)
    elif action == "Drop":
        if item in items:
            items.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(':')
        if old_item in items:
            idx = items.index(old_item)
            items.insert(idx + 1, new_item)
    elif action == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)

    command = input()
# End of Logic

# Print Output
print(*items, sep=', ')
