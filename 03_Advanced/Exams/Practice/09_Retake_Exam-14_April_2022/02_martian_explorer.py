def get_position(num):
    if num < 0:
        return 5
    elif num > 5:
        return 0
    else:
        return num


field = []
is_water = False
is_metal = False
is_concrete = False
ie, je = None, None
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(6):
    row = input().split()
    field.append(row)

    if 'E' in row:
        ie, je = i, row.index('E'),

moves = input().split(", ")

for m in moves:
    ie = get_position(ie + directions[m][0])
    je = get_position(je + directions[m][1])

    if field[ie][je] == 'R':
        print(f"Rover got broken at ({ie}, {je})")
        break
    elif field[ie][je] == 'W':
        print(f"Water deposit found at ({ie}, {je})")
        is_water = True
    elif field[ie][je] == 'M':
        print(f"Metal deposit found at ({ie}, {je})")
        is_metal = True
    elif field[ie][je] == 'C':
        print(f"Concrete deposit found at ({ie}, {je})")
        is_concrete = True

if is_concrete and is_metal and is_water:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
