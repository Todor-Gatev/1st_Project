legendary_materials = ("shards", "fragments", "motes")
qty = 0
all_materials = dict.fromkeys(legendary_materials, qty)
legendary_farms = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary_item = ""
is_enough_qty = False

while not is_enough_qty:
    data = input().lower().split()
    for i in range(0, len(data), 2):
        qty = int(data[i])
        material = data[i + 1]

        if material in legendary_materials:
            all_materials[material] += qty
            if all_materials[material] >= 250:
                all_materials[material] -= 250
                legendary_item = legendary_farms[material]
                is_enough_qty = True
                break
            continue

        if material not in all_materials:
            all_materials[material] = 0
        all_materials[material] += qty

print(f"{legendary_item} obtained!")

for material, qty in all_materials.items():
    print(f"{material}: {qty}")
