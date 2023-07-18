rows, columns = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]
counter = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        el_0_0 = matrix[row][column]
        el_0_1 = matrix[row][column + 1]
        el_1_0 = matrix[row + 1][column]
        el_1_1 = matrix[row + 1][column + 1]

        if el_0_0 == el_0_1 == el_1_0 == el_1_1:
            counter += 1

print(counter)
