n, m = [int(x) for x in input().split()]

player_cell = tuple()
bunnies = set()
won = True
directions = {
    "L": lambda x, y: [x, y - 1],
    "R": lambda x, y: [x, y + 1],
    "U": lambda x, y: [x - 1, y],
    "D": lambda x, y: [x + 1, y],
}

for i in range(n):
    row = list(input())

    for j in range(m):
        if row[j] == "B":
            bunnies.add((i, j))
        elif row[j] == "P":
            player_cell = (i, j)

for ch in list(input()):
    new_bunnies = set()

    for b in bunnies:
        new_bunnies.add((b[0] + 1, b[1])) if b[0] + 1 in range(n) else None
        new_bunnies.add((b[0] - 1, b[1])) if b[0] - 1 in range(n) else None
        new_bunnies.add((b[0], b[1] + 1)) if b[1] + 1 in range(m) else None
        new_bunnies.add((b[0], b[1] - 1)) if b[1] - 1 in range(m) else None

    bunnies.update(new_bunnies)

    i_player_new, j_player_new = directions[ch](*player_cell)

    if i_player_new in range(n) and j_player_new in range(m):
        player_cell = (i_player_new, j_player_new)

        if player_cell in bunnies:
            won = False
            break
    else:
        break

for i in range(n):
    for j in range(m):
        print("B", end='') if (i, j) in bunnies else print(".", end='')

    print()

if won:
    print("won:", *player_cell)
else:
    print("dead:", *player_cell)
