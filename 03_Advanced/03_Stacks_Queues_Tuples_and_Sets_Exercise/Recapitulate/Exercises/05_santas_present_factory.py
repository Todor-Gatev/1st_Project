from collections import deque

box_with_materials = list(map(int, input().split()))
magic_value = deque([int(x) for x in input().split()])

toys = {}
needed_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while box_with_materials and magic_value:
    material = box_with_materials.pop()
    magic = magic_value.popleft()

    result = magic * material

    if result in needed_magic:
        toys[needed_magic[result]] = toys.get(needed_magic[result], 0) + 1
    elif result < 0:
        box_with_materials.append(material + magic)
    elif result > 0:
        box_with_materials.append(material + 15)
    else:
        None if magic == 0 else magic_value.appendleft(magic)
        None if material == 0 else box_with_materials.append(material)

if {"Doll", "Wooden train"}.issubset(toys) or {"Bicycle", "Teddy bear"}.issubset(toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if box_with_materials:
    box_with_materials.reverse()
    print(f"Materials left: {', '.join(str(x) for x in box_with_materials)}")

if magic_value:
    print(f"Magic left: {', '.join(str(x) for x in magic_value)}")

for toy, amount in sorted(toys.items()):
    print(f"{toy}: {amount}")
