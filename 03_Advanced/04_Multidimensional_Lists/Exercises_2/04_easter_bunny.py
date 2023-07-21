def find_bunny_and_eggs_positions(field_f):
    bunny_row, bunny_col = None, None
    eggs_f = set()

    for row_f in range(n):
        for col_f in range(n):
            if field_f[row_f][col_f] == 'P':
                bunny_row, bunny_col = row_f, col_f
            elif field_f[row_f][col_f] == 'B':
                eggs_f.add((row_f, col_f))

    return bunny_row, bunny_col, eggs_f


n = int(input())
field = [list(input()) for _ in range(n)]
