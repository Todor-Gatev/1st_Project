plants = {}

for _ in range(int(input())):
    name, rarity = input().split("<->")
    plants.update({name: [rarity, []]})


while True:
    command = input()

    if command == "Exhibition":
        break

    action, data = command.split(": ")
    data = data.split(" - ")
    name = data[0]

    if name not in plants:
        print("error")
    elif action == "Rate":
        rating = int(data[1])
        plants[name][1].append(rating)
    elif action == "Update":
        new_rarity = data[1]
        plants[name][0] = new_rarity
    elif action == "Reset":
        plants[name][1].clear()

print("Plants for the exhibition:")

for name, info in plants.items():
    average_rating = 0

    if info[1]:
        average_rating = sum(info[1]) / len((info[1]))

    print(f"- {name}; Rarity: {info[0]}; Rating: {average_rating:.2f}")
