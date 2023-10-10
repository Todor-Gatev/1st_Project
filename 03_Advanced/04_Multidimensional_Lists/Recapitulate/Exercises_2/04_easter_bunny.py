n = int(input())

i_bunny, j_bunny = None, None
field = []
max_eggs = -float("inf")
is_bunny_cell_found = False
result = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    field.append(input().split())

    if not is_bunny_cell_found:
        if 'B' in field[i]:
            i_bunny, j_bunny = i, field[i].index('B')
            is_bunny_cell_found = True

for way, di_dj in directions.items():
    eggs = 0
    cells_with_eggs_on_way = []
    di, dj = di_dj
    row, col = i_bunny + di, j_bunny + dj
    found_eggs = False

    while row in range(n) and col in range(n):
        if field[row][col] == 'X':
            break

        found_eggs = True
        eggs += int(field[row][col])
        cells_with_eggs_on_way.append([row, col])
        row, col = row + di, col + dj

    if max_eggs < eggs and found_eggs:
        max_eggs = eggs
        result.clear()
        result.append(way)
        result.extend(cells_with_eggs_on_way)
        result.append(eggs)

print(*result, sep='\n')
