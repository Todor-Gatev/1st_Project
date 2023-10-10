n = int(input())

i_alice, j_alice = None, None
territory = []
tee_bags = 0
alice_cell_found = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    territory.append(input().split())

    if not alice_cell_found:
        if 'A' in territory[i]:
            alice_cell_found = True
            i_alice, j_alice = i, territory[i].index('A')
            territory[i_alice][j_alice] = '*'

while tee_bags < 10:
    di, dj = directions[input()]
    i_alice, j_alice = i_alice + di, j_alice + dj

    if i_alice not in range(n) or j_alice not in range(n):
        break

    value = territory[i_alice][j_alice]
    territory[i_alice][j_alice] = '*'

    if value == 'R':
        break

    tee_bags += int(value) if value.isdigit() else 0

if tee_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in territory]
