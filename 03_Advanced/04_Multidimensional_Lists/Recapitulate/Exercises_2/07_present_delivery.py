def cookies_case(x, y, gifts, kids):
    if neighborhood[x][y] == 'X':
        gifts -= 1
    elif neighborhood[x][y] == 'V':
        kids -= 1
        gifts -= 1

    neighborhood[x][y] = '-'

    return gifts, kids


presents = int(input())
size_of_neighborhood = int(input())
sad_nice_kids = 0
nice_kids = 0
neighborhood = []
r, c = None, None
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1,),
    "right": (0, 1),
}

for i in range(size_of_neighborhood):
    neighborhood.append(input().split())
    sad_nice_kids += neighborhood[i].count('V')
    nice_kids = sad_nice_kids

    if 'S' in neighborhood[i]:
        r, c = i, neighborhood[i].index('S')

while presents:
    command = input()

    if command == "Christmas morning":
        break

    di, dj = directions[command]

    if r + di in range(size_of_neighborhood) and c + dj in range(size_of_neighborhood):
        neighborhood[r][c] = '-'
        r, c, = r + di, c + dj

        if neighborhood[r][c] == 'V':
            sad_nice_kids -= 1
            presents -= 1
        elif neighborhood[r][c] == 'C':
            for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                presents, sad_nice_kids = cookies_case(i, j, presents, sad_nice_kids)

        neighborhood[r][c] = 'S'

if sad_nice_kids and not presents:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if sad_nice_kids:
    print(f"No presents for {sad_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
