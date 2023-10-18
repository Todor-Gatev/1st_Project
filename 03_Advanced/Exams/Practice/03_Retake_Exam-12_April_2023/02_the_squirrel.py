n = int(input())
commands = input().split(", ")

hazelnuts = 0
si, sj = None, None
field = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    row = list(input())
    field.append(row)

    if 's' in row:
        si, sj = i, row.index('s')

for c in commands:
    si, sj = si + moves[c][0], sj + moves[c][1]

    if si not in range(n) or sj not in range(n):
        print("The squirrel is out of the field.")
        break
    elif field[si][sj] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif field[si][sj] == 'h':
        field[si][sj] = '*'
        hazelnuts += 1

        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
