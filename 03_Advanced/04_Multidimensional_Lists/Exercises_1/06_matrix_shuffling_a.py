def are_valid_indexes(iterable):
    if len(iterable) != 4:
        return False

    return {iterable[0], iterable[2]}.issubset(range(row)) and {iterable[1], iterable[3]}.issubset(range(col))


row, col = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(row)]

command = input()

while command != "END":
    action, *indexes = [int(x) if x.isdigit() else x for x in command.split()]

    if action != "swap" or not are_valid_indexes(indexes):
        print("Invalid input!")
    else:
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*matrix[i]) for i in range(row)]

    command = input()
