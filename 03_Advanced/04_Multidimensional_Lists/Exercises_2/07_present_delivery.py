def get_santa_nice_kids_naughty_kids_positions():
    santa_row_f, santa_col_f = None, None
    nice_kids_f = set()
    naughty_kids_f = set()

    for row_f in range(size):
        neighborhood.append(input().split())

        if {'V', 'X', 'S'}.intersection(neighborhood[row_f]):
            for col_f in range(size):
                if neighborhood[row_f][col_f] == 'V':
                    nice_kids_f.add((row_f, col_f))
                elif neighborhood[row_f][col_f] == 'X':
                    naughty_kids_f.add((row_f, col_f))
                elif neighborhood[row_f][col_f] == 'S':
                    santa_row_f, santa_col_f = row_f, col_f

    return santa_row_f, santa_col_f, nice_kids_f, naughty_kids_f


def check_cookie_case():
    presents_f = 0

    for dx_dy in directions.values():
        row_f, col_f = row + dx_dy[0], col + dx_dy[1]
        if (row_f, col_f) in nice_kids.union(naughty_kids):
            presents_f += 1
            neighborhood[row_f][col_f] = '-'

            if (row_f, col_f) in nice_kids:
                nice_kids.remove((row_f, col_f))
            else:
                naughty_kids.remove((row_f, col_f))

    return presents_f


presents = int(input())
size = int(input())

neighborhood = []
santa_row, santa_col, nice_kids, naughty_kids = get_santa_nice_kids_naughty_kids_positions()
count_nice_kids = len(nice_kids)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


while presents and nice_kids.union(naughty_kids):
    command = input()

    if command == "Christmas morning":
        break

    row, col = santa_row + directions[command][0], santa_col + directions[command][1]

    if not (row in range(size) and col in range(size)):
        command = input()
        continue

    if neighborhood[row][col] == 'V':
        presents -= 1
        nice_kids.remove((row, col))
    elif neighborhood[row][col] == 'X':
        naughty_kids.remove((row, col))
    elif neighborhood[row][col] == 'C':
        presents -= check_cookie_case()

    neighborhood[santa_row][santa_col] = '-'
    neighborhood[row][col] = 'S'
    santa_row, santa_col = row, col

if not presents and nice_kids:
    print("Santa ran out of presents!")

[print(*neighborhood[row]) for row in range(size)]

if not nice_kids:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")
