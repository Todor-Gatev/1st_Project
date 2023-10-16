n, m = [int(x) for x in input().split()]

field = []
start_i, start_j = None, None
is_pizza_collected = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for r in range(n):
    row = list(input())
    field.append(row)

    if 'B' in row:
        start_i, start_j = r, row.index('B')

i_boy, j_boy = start_i, start_j

while True:
    di, dj = directions[input()]

    if i_boy + di not in range(n) or j_boy + dj not in range(m):
        print("The delivery is late. Order is canceled.")
        field[start_i][start_j] = ' '
        break
    elif field[i_boy + di][j_boy + dj] != '*':
        i_boy += di
        j_boy += dj

        if field[i_boy][j_boy] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            field[i_boy][j_boy] = 'R'
            is_pizza_collected = True
        elif field[i_boy][j_boy] == 'A':
            if is_pizza_collected:
                field[i_boy][j_boy] = 'P'
                field[start_i][start_j] = 'B'
                print("Pizza is delivered on time! Next order...")
                break
        else:
            field[i_boy][j_boy] = '.'

[print(*row, sep='') for row in field]
