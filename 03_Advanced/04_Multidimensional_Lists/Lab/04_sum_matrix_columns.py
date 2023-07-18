rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for i in range(columns):
    result = 0
    for j in range(rows):
        result += matrix[j][i]

    print(result)
