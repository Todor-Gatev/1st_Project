n = int(input())

bunny = [None, None]
field = []

for i in range(n):
    field.append(input().split())

    if 'B' in field[i]:
        bunny[0], bunny[1] = i, field[i].index('B')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

result = []
max_eggs = float("-inf")

for direction, dx_dy in directions.items():
    eggs = 0
    current_data = []
    row, col = bunny[0] + dx_dy[0], bunny[1] + dx_dy[1]
    are_collected_eggs = False

    while col in range(n) and row in range(n):
        if field[row][col] == 'X':
            break

        are_collected_eggs = True
        eggs += int(field[row][col])
        current_data.append([row, col])
        row, col = row + dx_dy[0], col + dx_dy[1]

    if max_eggs < eggs and are_collected_eggs:
        max_eggs = eggs
        result.clear()
        result.append(direction)
        result.extend(current_data)
        result.append(eggs)

print(*result, sep='\n')
