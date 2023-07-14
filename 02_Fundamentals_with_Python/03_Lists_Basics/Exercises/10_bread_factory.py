# Read user input
events = input().split('|')

# Variables
energy = 100
coins = 100
is_managed = True

# Logic
for el in events:
    el_list = el.split('-')

    if el_list[0] == "rest":
        temp_energy = energy + int(el_list[1])
        if temp_energy > 100:
            temp_energy = 100
        gained_energy = temp_energy - energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {temp_energy}.")
        energy = temp_energy
    elif el_list[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += int(el_list[1])
            print(f"You earned {int(el_list[1])} coins.")
        else:
            temp_energy = energy + 50
            if temp_energy > 100:
                temp_energy = 100
            energy = temp_energy
            print("You had to rest!")
            # is_managed = False
    else:
        if coins >= int(el_list[1]):
            coins -= int(el_list[1])
            print(f"You bought {el_list[0]}.")
        else:
            print(f"Closed! Cannot afford {el_list[0]}.")
            is_managed = False
            break
# End of Logic

# Print Output
if is_managed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
