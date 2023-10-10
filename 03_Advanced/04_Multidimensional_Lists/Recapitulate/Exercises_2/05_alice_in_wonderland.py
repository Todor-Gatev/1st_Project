def print_result(iterable, found):
    if found:
        print("She did it! She went to the party.")
    else:
        print("Alice didn't make it to the tea party.")

    [print(*line) for line in iterable]


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

while True:
    di, dj = directions[input()]
    i_alice, j_alice = i_alice + di, j_alice + dj

    if i_alice not in range(n) or j_alice not in range(n):
        print_result(territory, 0)
        exit()  # or break

    value = territory[i_alice][j_alice]
    territory[i_alice][j_alice] = '*'

    if value == 'R':
        print_result(territory, 0)
        break  # or exit

    tee_bags += int(value) if value.isdigit() else 0

    if tee_bags >= 10:
        print_result(territory, 1)
        exit()  # or break
