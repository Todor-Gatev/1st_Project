def find_knights(board_f):
    knights_f = []

    for i_f in range(n):
        for j_f in range(n):
            if board_f[i_f][j_f] == 'K':
                knights_f.append((i_f, j_f))

    return knights_f


def get_knight_range(knight_f):
    x, y = knight_f
    return {(x + dx, y + dy)
            for h, v in [(1, 2), (2, 1)]  # range
            for dx, dy in [(h, v), (h, -v), (-h, v), (-h, -v)]}  # directions
#            if x + dx in range(1, n) and y + dy in range(1, n)}  # in-board


n = int(input())
board = [list(input()) for _ in range(n)]

knights = find_knights(board)
removed_knights = 0
is_attack_available = True

while is_attack_available:
    knight_to_be_removed = None
    max_attacks = 0
    is_attack_available = False

    for knight in knights:
        knight_range = get_knight_range(knight)
        knight_attacks = len(knight_range.intersection(knights))

        if max_attacks < knight_attacks:
            knight_to_be_removed = knight
            max_attacks = knight_attacks
            is_attack_available = True

        knight_range.clear()

    if knight_to_be_removed:
        knights.remove(knight_to_be_removed)
        removed_knights += 1

print(removed_knights)
