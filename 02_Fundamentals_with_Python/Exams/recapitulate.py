plants = {}

for _ in range(int(input())):
    plant, rarity = input().split("<->")
    plants.update({plant: [rarity, []]})

while True:
    command = input()

    if command == "Exhibition":
        break

    command = command.split(": ")
    action = command[0]
    info = command[1].split(" - ")
    plant = info[0]

    if plant not in plants:
        print("error")
    elif action == "Rate":
        rating = int(info[1])
        plants[plant][1].append(rating)
    elif action == "Update":
        new_rarity = info[1]
        plants[plant][0] = new_rarity
    elif action == "Reset":
        plants[plant][1] = []

print("Plants for the exhibition:")

for plant, values in plants.items():
    if not values[1]:
        average_rating = 0
    else:
        average_rating = sum(values[1]) / len(values[1])

    print(f"- {plant}; Rarity: {values[0]}; Rating: {average_rating:.2f}")
