# Read user input
elements = input().split()

# Variables
moves = 0

# Logic
while elements:
    command = input()

    if command == "end":
        print("Sorry you lose :(")
        print(' '.join(elements))
        break

    moves += 1
    # index1, index2 = [int(x) for x in command.split()]
    index = [int(x) for x in command.split()]
    index1 = max(index)
    index2 = min(index)

    if index2 == index1 or \
            max(index1, index2) >= len(elements) or \
            min(index1, index2) < 0:
        elements.insert(len(elements) // 2, f"-{moves}a")
        elements.insert(len(elements) // 2, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index2]}!")
        elements.pop(index1), elements.pop(index2)
    else:
        print("Try again!")
else:
    print(f"You have won in {moves} turns!")
# End of Logic

# Print Output
