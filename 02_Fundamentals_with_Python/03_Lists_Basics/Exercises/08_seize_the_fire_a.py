# Read user input
level_of_fire = input().split('#')
water = int(input())

# Variables
efforts = 0
cells = []
total_fire = 0

# Logic
for el in level_of_fire:
    if water < 1:
        break

    el_list = el.split(' = ')

    if water < int(el_list[1]):
        continue

    if (el_list[0] == "High" and 81 <= int(el_list[1]) <= 125) \
            or (el_list[0] == "Medium" and 51 <= int(el_list[1]) <= 80) \
            or (el_list[0] == "Low" and 1 <= int(el_list[1]) <= 50):
        water -= int(el_list[1])
        efforts += int(el_list[1]) * 0.25
        cells.append(el_list[1])
        total_fire += int(el_list[1])
# End of Logic

# Print Output
if not cells:
    print("Cells:")
else:
    print("Cells:\n - ", end='')
    print("\n - ".join(x for x in cells))

print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {total_fire}")
