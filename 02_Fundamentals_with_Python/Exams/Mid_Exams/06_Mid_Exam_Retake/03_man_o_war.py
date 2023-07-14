def is_idx(iterable_f, idx_f):
    return 0 <= idx_f < len(iterable_f)


# Read user input
pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input()

# Variables

# Logic
while command != "Retire":
    command = command.split()
    action = command[0]
    if action == "Fire":
        idx = int(command[1])
        damage = int(command[2])
        if is_idx(warship, idx):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif action == "Defend":
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if 0 <= start_idx and end_idx < len(pirate_ship):
            for idx in range(start_idx, end_idx + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif action == "Repair":
        idx = int(command[1])
        repair = int(command[2])
        if is_idx(pirate_ship, idx):
            pirate_ship[idx] += repair
            pirate_ship[idx] = min(max_health, pirate_ship[idx])
    elif action == "Status":
        count = 0
        for_repair = 0.20 * max_health

        for section in pirate_ship:
            if section < for_repair:
                count += 1

        print(f"{count} sections need repair.")
    command = input()
# End of Logic

# Print Output
print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
