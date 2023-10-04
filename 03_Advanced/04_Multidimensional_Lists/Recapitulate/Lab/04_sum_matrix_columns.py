row, column = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(row)]

for j in range(column):
    print(sum(matrix[i][j] for i in range(row)))
