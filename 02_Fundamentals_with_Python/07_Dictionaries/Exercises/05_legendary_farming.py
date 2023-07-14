junk = {}
legendary_item = ""
is_reached = False
materials = {"shards": ["Shadowmourne", 0],
             "fragments": ["Valanyr", 0],
             "motes": ["Dragonwrath", 0]
             }

while not is_reached:
    data = input().lower().split()
    for i in range(0, len(data), 2):
        value = int(data[i])
        key = data[i + 1]
        if key in materials:
            materials[key][1] += value
            if materials[key][1] >= 250:
                materials[key][1] -= 250
                legendary_item = materials[key][0]
                is_reached = True
                break
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value

print(f"{legendary_item} obtained!")

for key, value in materials.items():
    print(f"{key}: {value[1]}")

for key, value in junk.items():
    print(f"{key}: {value}")
