row, col = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(row)]
result = 0

for i in range(row - 1):
    for j in range(col - 1):
        el_0_0 = matrix[i][j]
        el_1_0 = matrix[i + 1][j]
        el_0_1 = matrix[i][j + 1]
        el_1_1 = matrix[i + 1][j + 1]

        if el_0_0 == el_1_0 == el_0_1 == el_1_1:
            result += 1

print(result)
