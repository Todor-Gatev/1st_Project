n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs = input().split()
alive_cells = 0
sum_of_cells = 0

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    damage = matrix[row][col]
    if damage > 0:
        for i in range(row - 1, row + 2):
            if i in range(n):
                for j in range(col - 1, col + 2):
                    if j in range(n):
                        if matrix[i][j] > 0:
                            matrix[i][j] -= damage

        matrix[row][col] = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            alive_cells += 1
            sum_of_cells += matrix[i][j]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
[print(*matrix[row]) for row in range(n)]
