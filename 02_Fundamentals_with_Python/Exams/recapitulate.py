targets = {}

while True:
    command = input()

    if command == "Sail":
        break

    command = command.split("||")
    city = command[0]
    population, gold = int(command[1]), int(command[2]),

    if city not in targets:
        targets[city] = [0, 0]

    targets[city][0] += population
    targets[city][1] += gold

while True:
    command = input()

    if command == "End":
        break

    action, town, *info = command.split("=>")

    if action == "Plunder":
        people, gold = int(info[0]), int(info[1]),
        targets[town][0] -= people
        targets[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets[town][0] == 0 or targets[town][1] == 0:
            targets.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        gold = int(info[0])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targets[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.")

if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")

    for town, info in targets.items():
        print(f"{town} -> Population: {info[0]} citizens, Gold: {info[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
