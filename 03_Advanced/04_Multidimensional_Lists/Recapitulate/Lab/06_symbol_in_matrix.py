n = int(input())
matrix = [list(input()) for _ in range(n)]
symbol = input()

for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            exit()
else:
    print(f"{symbol} does not occur in the matrix")
