def find_components(field_f):
    i_start, j_start = 0, 0
    coals_f = []
    route_end_f = tuple()
    for i_f in range(n):
        for j_f in range(n):
            if field_f[i_f][j_f] == 's':
                i_start, j_start = i_f, j_f
            elif field_f[i_f][j_f] == 'e':
                route_end_f = (i_f, j_f)
            elif field_f[i_f][j_f] == 'c':
                coals_f.append((i_f, j_f))

    return i_start, j_start, route_end_f, coals_f


def get_new_position(action_f, row_f, col_f):
    if action_f == "left":
        if col_f - 1 >= 0:
            col_f -= 1
    elif action_f == "right":
        if col_f + 1 < n:
            col_f += 1
    elif action_f == "up":
        if row_f - 1 >= 0:
            row_f -= 1
    elif action_f == "down":
        if row_f + 1 < n:
            row_f += 1

    return row_f, col_f


n = int(input())
commands = input().split()
field = [input().split() for _ in range(n)]

row, col, route_end, coals = find_components(field)

for action in commands:
    row, col = get_new_position(action, row, col)
    if (row, col) == route_end:
        print(f"Game over! {route_end}")
        exit()
    elif (row, col) in coals:
        coals.remove((row, col))
        if not coals:
            print(f"You collected all coal! ({row}, {col})")
            exit()

print(f"{len(coals)} pieces of coal left. ({row}, {col})")
