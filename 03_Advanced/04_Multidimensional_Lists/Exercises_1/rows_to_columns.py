matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

new_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        cur_el = matrix[row][col]
        new_matrix[2 - col][row] = cur_el

print(new_matrix)
matrix = new_matrix
