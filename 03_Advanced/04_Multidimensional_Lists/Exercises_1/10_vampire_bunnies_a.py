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


def print_final_lair(bunnies_f):
    for i in range(row):
        for j in range(col):
            if (i, j) in bunnies_f:
                print("B", end='')
            else:
                print(".", end='')
        print()


def spread_bunnies(bunnies_f):
    bunnies_spread = set()
    for bunny in bunnies_f:
        bunnies_spread.add((bunny[0] - 1, bunny[1]))
        bunnies_spread.add((bunny[0] + 1, bunny[1]))
        bunnies_spread.add((bunny[0], bunny[1] - 1))
        bunnies_spread.add((bunny[0], bunny[1] + 1))

    return bunnies_spread


row, col = [int(x) for x in input().split()]
lair = [list(input()) for _ in range(row)]
moves = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

p_row, p_col, bunnies = find_p_b_positions(lair)

for move in moves:

    bunnies.update(spread_bunnies(bunnies))
    p_row_new, p_col_new = p_row + directions[move][0], p_col + directions[move][1]

    if not (p_row_new in range(row) and p_col_new in range(col)):
        print_final_lair(bunnies)
        print(f"won: {p_row} {p_col}")
        exit()
    elif (p_row_new, p_col_new) in bunnies:
        print_final_lair(bunnies)
        print(f"dead: {p_row_new} {p_col_new}")
        exit()

    p_row, p_col = p_row_new, p_col_new
