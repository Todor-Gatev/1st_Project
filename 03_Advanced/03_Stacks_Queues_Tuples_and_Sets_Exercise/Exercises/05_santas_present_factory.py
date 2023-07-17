from collections import deque
from collections import defaultdict

materials = list(map(int, input().split()))
magic_values = deque(map(int, input().split()))

needed_magic = [150, 250, 300, 400]
crafted = defaultdict(list)

map_functions = {
    150: lambda x: crafted["Doll"].append(1),
    250: lambda x: crafted["Wooden train"].append(1),
    300: lambda x: crafted["Teddy bear"].append(1),
    400: lambda x: crafted["Bicycle"].append(1)
}

while materials and magic_values:
    material = materials.pop()
    magic_value = magic_values.popleft()
    magic = material * magic_value
    if magic in needed_magic:
        map_functions[magic](None)
    elif magic < 0:
        materials.append(material + magic_value)
    elif magic > 0:
        materials.append(material + 15)
    else:
        if material != 0:
            materials.append(material)

        if magic_value != 0:
            magic_values.appendleft(magic_value)

# if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")

if "Doll" in crafted and "Wooden train" in crafted or \
        "Teddy bear" in crafted and "Bicycle" in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end='')
    print(*materials[::-1], sep=", ")
elif magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for present, qty in sorted(crafted.items()):
    print(f"{present}: {len(qty)}")
