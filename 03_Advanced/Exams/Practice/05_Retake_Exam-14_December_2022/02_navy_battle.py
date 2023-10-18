n = int(input())

battlefield = []
si, sj = None, None
hits_num = 0
cruisers = 3
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    row = list(input())
    battlefield.append(row)

    if 'S' in row:
        si, sj = i, row.index('S'),

while cruisers and hits_num < 3:
    battlefield[si][sj] = '-'
    move = input()
    si, sj = si + directions[move][0], sj + directions[move][1],

    if battlefield[si][sj] == '*':
        hits_num += 1
    elif battlefield[si][sj] == 'C':
        cruisers -= 1

    battlefield[si][sj] = 'S'

if cruisers:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{si}, {sj}]!")
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

[print(*row, sep='') for row in battlefield]
