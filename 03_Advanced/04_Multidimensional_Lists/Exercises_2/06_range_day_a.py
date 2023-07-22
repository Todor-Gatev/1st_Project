def get_field_targets_and_my_position():
    field_f, targets_f = [], []
    my_row_f, my_col_f = None, None

    for row_f in range(n):
        field_f.append(input().split())

        if 'A' in field_f[row_f]:
            my_row_f, my_col_f = row_f, field_f[row_f].index('A')
            field_f[my_row_f][my_col_f] = '.'

        if 'x' in field_f[row_f]:
            for col_f in range(n):
                if field_f[row_f][col_f] == 'x':
                    targets_f.append((row_f, col_f))

    return field_f, targets_f, my_row_f, my_col_f


n = 5
field, targets, my_row, my_col = get_field_targets_and_my_position()
hit_targets = []

directions = {
    "up": lambda x: (-x, 0),
    "down": lambda x: (x, 0),
    "left": lambda x: (0, -x),
    "right": lambda x: (0, x),
}

for _ in range(int(input())):
    if not targets:
        break

    command = input().split()
    action, direction = command[0], command[1],

    if action == "shoot":
        row, col = my_row + directions[direction](1)[0], my_col + directions[direction](1)[1]

        while row in range(n) and col in range(n):

            if (row, col) in targets:
                hit_targets.append([row, col])
                targets.remove((row, col))
                field[row][col] = '.'
                break

            row, col = row + directions[direction](1)[0], col + directions[direction](1)[1]
    elif action == "move":
        steps = int(command[2])
        for i in range(steps, 0, -1):
            row, col = my_row + directions[direction](i)[0], my_col + directions[direction](i)[1]

            if row in range(n) and col in range(n) and field[row][col] == '.':
                my_row, my_col = row, col
                break

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")

print(*hit_targets, sep='\n')
