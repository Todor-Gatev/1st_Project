# Read user input
energy = int(input())
command = input()

# Variables
count = 0

# Logic
while command != "End of battle":
    distance = int(command)

    if energy < distance:
        print(f"Not enough energy! Game ends with {count} won battles"
              f" and {energy} energy")
        exit()

    energy -= distance
    count += 1

    if count % 3 == 0:
        energy += count

    command = input()
# End of Logic

# Print Output
print(f"Won battles: {count}. Energy left: {energy}")
