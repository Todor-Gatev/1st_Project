def find_p_b_positions(lair_f):
    p_i_start, p_j_start = None, None
    bunnies_f = set()
    for i_f in range(row):
        for j_f in range(col):
            if lair_f[i_f][j_f] == 'P':
                p_i_start, p_j_start = i_f, j_f
            elif lair_f[i_f][j_f] == 'B':
                bunnies_f.add((i_f, j_f))

    return p_i_start, p_j_start, bunnies_f


def get_new_position(move_f, row_f, col_f):
    if move_f == "L":
        col_f -= 1
    elif move_f == "R":
        col_f += 1
    elif move_f == "U":
        row_f -= 1
    elif move_f == "D":
        row_f += 1

    return row_f, col_f


def print_final_lair(bunnies_f):
    for i in range(row):
        for j in range(col):
            if (i, j) in bunnies_f:
                print("B", end='')
            else:
                print(".", end='')
        print()


row, col = [int(x) for x in input().split()]
lair = [list(input()) for _ in range(row)]
moves = input()

p_row, p_col, bunnies_temp = find_p_b_positions(lair)
bunnies = bunnies_temp.copy()

for move in moves:
    for bunny in bunnies:
        bunnies_temp.add((bunny[0] - 1, bunny[1]))
        bunnies_temp.add((bunny[0] + 1, bunny[1]))
        bunnies_temp.add((bunny[0], bunny[1] - 1))
        bunnies_temp.add((bunny[0], bunny[1] + 1))

    bunnies.update(bunnies_temp)
    p_row_new, p_col_new = get_new_position(move, p_row, p_col)

    if p_row_new not in range(row) or p_col_new not in range(col):
        print_final_lair(bunnies)
        print(f"won: {p_row} {p_col}")
        exit()
    elif (p_row_new, p_col_new) in bunnies:
        print_final_lair(bunnies)
        print(f"dead: {p_row_new} {p_col_new}")
        exit()

    p_row, p_col = p_row_new, p_col_new
