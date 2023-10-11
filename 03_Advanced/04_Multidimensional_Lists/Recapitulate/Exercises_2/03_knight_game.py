n = int(input())

knights = []
removed_knights = 0
# positions = tuple([(i, j) for v, h in [[1, 2], [2, 1]] for i, j in [[v, h], [v, -h], [-v, h], [-v, -h]]])
positions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2))

for i in range(n):
    row = list(input())

    for j in range(n):
        if row[j] == 'K':
            knights.append((i, j))

while True:
    max_attacks = 0
    knight_to_be_removed = None

    for knight in knights:
        i, j = knight
        # possible_moves = {(i + di, j + dj)
        #                   for v, h in [[1, 2], [2, 1]]
        #                   for di, dj in [[v, h], [v, -h], [-v, h], [-v, -h]]
        #                   if i + di in range(n) and j + dj in range(n)}  # this line could be omitted,
        # # because of the next line - possible_moves.intersection(knights)
        # knight_attacks = len(possible_moves.intersection(knights))

        # knight_attacks = len({(i + di, j + dj)
        #                       for v, h in [[1, 2], [2, 1]]
        #                       for di, dj in [[v, h], [v, -h], [-v, h], [-v, -h]]
        #                       if (i + di, j + dj) in knights})

        # knight_attacks = len({(i + di, j + dj) for di, dj in positions if (i + di, j + dj) in knights})
        knight_attacks = len({(i + di, j + dj) for di, dj in positions}.intersection(knights))  # intersection
        # this row is faster than the upper row due to intersection

        if max_attacks < knight_attacks:
            max_attacks = knight_attacks
            knight_to_be_removed = knight

    if knight_to_be_removed:
        knights.remove(knight_to_be_removed)
        removed_knights += 1
    else:
        print(removed_knights)
        exit()
