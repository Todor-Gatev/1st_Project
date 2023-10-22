def get_position(num, nf):
    if num < 0:
        return nf - 1
    elif num > nf - 1:
        return 0
    else:
        return num


n = int(input())

fishing_area = []
im, jm = None, None
collected_fish = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    row = list(input())
    fishing_area.append(row)

    if 'S' in row:
        im, jm = i, row.index('S'),

while True:
    action = input()

    if action == "collect the nets":
        break

    fishing_area[im][jm] = '-'

    im, jm = get_position(im + directions[action][0], n), get_position(jm + directions[action][1], n),

    if fishing_area[im][jm] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{im},{jm}]")
        exit()
    elif fishing_area[im][jm].isdigit():
        collected_fish += int(fishing_area[im][jm])

    fishing_area[im][jm] = "S"

if collected_fish < 20:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {20 - collected_fish} tons of fish more.")
else:
    print(f"Success! You managed to reach the quota!")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row, sep='') for row in fishing_area]
