n = int(input())

knights = []
board_cells = set()
removed_knights = 0

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

        knight_attacks = len({(i + di, j + dj)
                              for v, h in [[1, 2], [2, 1]]
                              for di, dj in [[v, h], [v, -h], [-v, h], [-v, -h]]
                              if (i + di, j + dj) in knights})

        if max_attacks < knight_attacks:
            max_attacks = knight_attacks
            knight_to_be_removed = knight

    if knight_to_be_removed:
        knights.remove(knight_to_be_removed)
        removed_knights += 1
    else:
        print(removed_knights)
        exit()
