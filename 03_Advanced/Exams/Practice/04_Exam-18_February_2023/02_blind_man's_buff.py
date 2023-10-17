n, m = [int(x) for x in input().split()]

playground = []
moves_made = 0
touched_opponents = 0
im, jm = None, None
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    row = input().split()
    playground.append(row)

    if 'B' in row:
        im, jm = i, row.index('B'),

while touched_opponents < 3:
    action = input()

    if action == "Finish":
        break

    di, dj = directions[action]
    r, c = im + di, jm + dj

    if r not in range(n) or c not in range(m) or playground[r][c] == 'O':
        continue

    im, jm = r, c

    if playground[im][jm] == 'P':
        playground[im][jm] = '-'
        touched_opponents += 1

    moves_made += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")
