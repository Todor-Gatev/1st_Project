IMPACT_RANGE = 1

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = [tuple(int(x) for x in y.split(',')) for y in input().split()]
dead_cells = set()

for cell in bombs:
    row, col = cell

    if matrix[row][col] == 0:
        continue

    bomb_power = matrix[row][col]
    matrix[row][col] = 0
    # attacked_cells.add((row, col))
    cells_i = set(range(row - IMPACT_RANGE, row + IMPACT_RANGE + 1)).intersection(range(n))
    cells_j = set(range(col - IMPACT_RANGE, col + IMPACT_RANGE + 1)).intersection(range(n))

    for i in cells_i:
        for j in cells_j:
            if (i, j) not in dead_cells:
                matrix[i][j] -= bomb_power
                dead_cells.add((i, j)) if matrix[i][j] <= 0 else None

print(f"Alive cells: {len([el for line in matrix for el in line if el > 0])}")
print(f"Sum: {sum(el for line in matrix for el in line if el > 0)}")
[print(*[num for num in row]) for row in matrix]
