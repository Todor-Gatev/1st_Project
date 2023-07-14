# Read user input
# integers = [int(x) for x in input().split()]
# command = input()
rooms = input().split('|')

# Variables
bitcoins = 0
health = 100
num_room = 0

# Logic
for room in rooms:
    num_room += 1
    data = room.split()
    action = data[0]
    amount = int(data[1])

    if action == "potion":
        if health + amount > 100:
            amount = 100 - health

        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount

        if 0 < health:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {num_room}")
            exit()
# End of Logic

# Print Output
print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
