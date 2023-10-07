rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = float('-inf')
sqr_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        first_row = matrix[row][column:column + 3]
        second_row = matrix[row + 1][column:column + 3]
        third_row = matrix[row + 2][column:column + 3]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if max_sum < current_sum:
            max_sum = current_sum
            sqr_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")

for i in range(3):
    print(*sqr_matrix[i])
