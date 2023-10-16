n, m = [int(x) for x in input().split(',')]

cupboard = []
mi, mj = None, None
cheese_num = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

for i in range(n):
    row = list(input())
    cheese_num += row.count('C')
    cupboard.append(row)

    if 'M' in row:
        mi, mj = i, row.index('M')

while True:
    action = input()

    if action == "danger":
        print("Mouse will come back later!")
        break

    di, dj = directions[action]

    if mi + di not in range(n) or mj + dj not in range(m):
        print("No more cheese for tonight!")
        break
    elif cupboard[mi + di][mj + dj] == '@':
        continue

    cupboard[mi][mj] = '*'
    mi, mj = mi + di, mj + dj

    if cupboard[mi][mj] == 'C':
        cheese_num -= 1
        cupboard[mi][mj] = 'M'

        if not cheese_num:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard[mi][mj] == 'T':
        cupboard[mi][mj] = 'M'
        print("Mouse is trapped!")
        break
    else:
        cupboard[mi][mj] = 'M'

[print(*row, sep='') for row in cupboard]
