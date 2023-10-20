matrix = [input().split() for _ in range(6)]
start_pos = input()

ci, cj = int(start_pos[1]), int(start_pos[4])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    action, *info = input().split(", ")

    if action == "Stop":
        break

    direction = info[0]
    ci, cj = ci + directions[direction][0], cj + directions[direction][1]

    if action == "Create":
        if matrix[ci][cj] == '.':
            matrix[ci][cj] = info[1]
    elif action == "Update":
        if matrix[ci][cj] != '.':
            matrix[ci][cj] = info[1]
    elif action == "Delete":
        matrix[ci][cj] = '.'
    elif action == "Read":
        if matrix[ci][cj] != '.':
            print(matrix[ci][cj])

[print(*row, sep=' ') for row in matrix]
