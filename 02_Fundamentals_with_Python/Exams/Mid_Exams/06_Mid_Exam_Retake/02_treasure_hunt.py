# Read user input
loot_items = input().split("|")
command = input()

# Variables

# Logic
while command != "Yohoho!":
    command = command.split()
    action = command[0]

    if action == "Loot":
        add_items = command[1:]
        for item in add_items:
            if item not in loot_items:
                loot_items.insert(0, item)
        # for idx in range(1, len(command)):
        #     item = command[idx]
        #     if item not in loot_items:
        #         loot_items.insert(0, item)
    elif action == "Drop":
        idx = int(command[1])
        if 0 <= idx < len(loot_items):
            item = loot_items.pop(idx)
            loot_items.append(item)
    elif action == "Steal":
        count = int(command[1])
        count = min(count, len(loot_items))
        left_items_num = len(loot_items) - count
        # print(', '.join(loot_items[left_items_num:]))
        print(*loot_items[left_items_num:], sep=', ')
        loot_items = loot_items[:left_items_num]
        # steal = []
        # for _ in range(count):
        #     steal.insert(0, loot_items[-1])
        #     loot_items.pop()
        #
        # print(*steal, sep=', ')
    command = input()
# End of Logic

# Print Output
if loot_items:
    # sum_of_len = 0
    # for item in loot_items:
    #     sum_of_len += len(item)
    sum_of_len = sum(len(item) for item in loot_items)
    average_gain = sum_of_len / len(loot_items)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
