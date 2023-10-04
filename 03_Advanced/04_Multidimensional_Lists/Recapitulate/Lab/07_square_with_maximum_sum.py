row, col = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]

biggest_sum = -float("inf")
result = []

for i in range(row - 1):
    for j in range(col - 1):
        el_0_0 = matrix[i][j]
        el_0_1 = matrix[i][j + 1]
        el_1_0 = matrix[i + 1][j]
        el_1_1 = matrix[i + 1][j + 1]

        temp_sum = el_0_0 + el_0_1 + el_1_0 + el_1_1

        if temp_sum > biggest_sum:
            biggest_sum = temp_sum
            result = [[el_0_0, el_0_1], [el_1_0, el_1_1]]

for i in range(2):
    print(*result[i])

print(biggest_sum)
