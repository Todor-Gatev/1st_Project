rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

sqr_matrix = []
max_sum = float('-inf')

for row in range(rows - 1):
    for column in range(columns - 1):
        el_0_0 = matrix[row][column]
        el_0_1 = matrix[row][column + 1]
        el_1_0 = matrix[row + 1][column]
        el_1_1 = matrix[row + 1][column + 1]
        current_sum = el_0_0 + el_0_1 + el_1_0 + el_1_1

        if current_sum > max_sum:
            max_sum = current_sum
            sqr_matrix = [[el_0_0, el_0_1], [el_1_0, el_1_1]]

for i in range(2):
    print(*sqr_matrix[i])
print(max_sum)
