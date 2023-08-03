# Variables
zoo = {}

# Logic
while True:
    command = input()

    if command == "EndDay":
        break

    action, info = command.split(": ")

    if action == "Add":
        name, needed_food_qty, area = info.split('-')
        needed_food_qty = int(needed_food_qty)

        if name not in zoo:
            zoo[name] = [0, area]

        zoo[name][0] += needed_food_qty
    elif action == "Feed":
        name, food = info.split('-')
        food = int(food)

        if name in zoo:
            zoo[name][0] -= food

            if zoo[name][0] <= 0:
                zoo.pop(name)
                print(f"{name} was successfully fed")
# End of Logic

# Print Output
areas = {}
print("Animals:")

for name, info in zoo.items():
    area = info[1]

    if area not in areas:
        areas[area] = 0

    areas[area] += 1

    print(f" {name} -> {info[0]}g")

print("Areas with hungry animals:")

for area, number in areas.items():
    print(f" {area}: {number}")
