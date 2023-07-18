row, col = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(row)]

command = input()

while command != "END":
    command = command.split()
    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        command = input()
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if row1 in range(row) and \
            row2 in range(row) and \
            col1 in range(col) and \
            col2 in range(col):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for i in range(row):
            print(*matrix[i])
    else:
        print("Invalid input!")
    command = input()
