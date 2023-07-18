rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

sqr_matrix = []
max_sum = float('-inf')

for row in range(rows - 1):
    for column in range(columns - 1):
        current_sum = 0
        temp_matrix = []
        temp_row = -1

        for i in range(row, row + 2):
            temp_row += 1
            temp_matrix.append([])
            for j in range(column, column + 2):
                current_sum += matrix[i][j]
                temp_matrix[temp_row].append(matrix[i][j])

        if current_sum > max_sum:
            max_sum = current_sum
            sqr_matrix = temp_matrix.copy()

for i in range(2):
    print(*sqr_matrix[i])
print(max_sum)
