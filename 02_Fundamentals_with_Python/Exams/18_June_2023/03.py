# Read user input
cards = input().split(", ")
n = int(input())

# Logic
for _ in range(n):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        name = command[1]
        if name in cards:
            print("Card is already in the deck")
        else:
            cards.append(name)
            print("Card successfully added")
    elif action == "Remove":
        name = command[1]
        if name in cards:
            print("Card successfully removed")
            cards.remove(name)
        else:
            print("Card not found")
    elif action == "Remove At":
        idx = int(command[1])
        if idx not in range(len(cards)):
            print("Index out of range")
        else:
            cards.pop(idx)
            print("Card successfully removed")
    elif action == "Insert":
        idx = int(command[1])
        name = command[2]

        if idx not in range(len(cards)):
            print("Index out of range")
        elif name in cards:
            print("Card is already added")
        else:
            cards.insert(idx, name)
            print("Card successfully added")
# End of Logic

# Print Output
print(*cards, sep=", ")
