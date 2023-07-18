n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

for row in range(n):
    for column in range(n):
        if matrix[row][column] == symbol:
            print(f"({row}, {column})")
            exit()
else:
    print(f"{symbol} does not occur in the matrix")
