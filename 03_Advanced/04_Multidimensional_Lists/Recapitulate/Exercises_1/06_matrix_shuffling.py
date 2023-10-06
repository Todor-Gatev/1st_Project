def are_idx_valid(iterable: list):
    if len(iterable) != 4:
        return False

    return {iterable[0], iterable[2]}.issubset(range(rows)) and {iterable[1], iterable[3]}.issubset(range(cols))


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

while True:
    action, *indexes = [int(x) if x.isdigit() else x for x in input().split()]

    if action == "END":
        break

    if action != "swap" or not are_idx_valid(indexes):
        print("Invalid input!")
    else:
        r1, c1, r2, c2 = indexes
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row) for row in matrix]
