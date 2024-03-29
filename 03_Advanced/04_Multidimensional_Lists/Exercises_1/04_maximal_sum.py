rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
sqr_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        current_sum = 0
        temp_matrix = []
        temp_row = -1
        for i in range(row, row + 3):
            temp_row += 1
            temp_matrix.append([])
            for j in range(column, column + 3):
                current_sum += matrix[i][j]
                temp_matrix[temp_row].append(matrix[i][j])

        if max_sum < current_sum:
            max_sum = current_sum
            sqr_matrix = temp_matrix.copy()

print(f"Sum = {max_sum}")

for i in range(3):
    print(*sqr_matrix[i])
