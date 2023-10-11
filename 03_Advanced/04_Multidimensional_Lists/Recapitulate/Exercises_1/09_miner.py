n = int(input())
commands = input().split()

miner_cell = []
coal_cells = []
e_cells = []
directions = {
    "left": lambda x, y: [x, y - 1] if y - 1 in range(n) else [x, y],
    "right": lambda x, y: [x, y + 1] if y + 1 in range(n) else [x, y],
    "up": lambda x, y: [x - 1, y] if x - 1 in range(n) else [x, y],
    "down": lambda x, y: [x + 1, y] if x + 1 in range(n) else [x, y],
}

for i in range(n):
    row = input().split()

    for j in range(len(row)):
        if row[j] == 'c':
            coal_cells.append([i, j])
        elif row[j] == 'e':
            e_cells.append([i, j])
        elif row[j] == 's':
            miner_cell = [i, j]

for command in commands:
    miner_cell = directions[command](miner_cell[0], miner_cell[1])

    if miner_cell in e_cells:
        print(f"Game over! ({miner_cell[0]}, {miner_cell[1]})")
        exit()
    elif miner_cell in coal_cells:
        coal_cells.remove(miner_cell)

        if not coal_cells:
            print(f"You collected all coal! ({miner_cell[0]}, {miner_cell[1]})")
            exit()

print(f"{len(coal_cells)} pieces of coal left. ({miner_cell[0]}, {miner_cell[1]})")
