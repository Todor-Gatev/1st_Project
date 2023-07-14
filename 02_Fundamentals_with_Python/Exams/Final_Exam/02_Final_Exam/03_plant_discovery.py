n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants.update({plant: [rarity]})

command = input()

while command != "Exhibition":
    command = command.split(': ')
    action = command[0]
    info = command[1].split(" - ")
    plant = info[0]

    if plant not in plants:
        print("error")
        command = input()
        continue

    if action == "Rate":
        rating = int(info[1])
        plants[plant].append(rating)
    elif action == "Update":
        new_rarity = info[1]
        plants[plant][0] = new_rarity
    elif action == "Reset":
        plants[plant] = plants[plant][:1]
    command = input()

print("Plants for the exhibition:")

for plant, info in plants.items():
    rarity = plants[plant][0]
    rating_list = plants[plant][1:]
    if not rating_list:
        average_rating = 0
    else:
        average_rating = sum(rating_list) / len(rating_list)
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
