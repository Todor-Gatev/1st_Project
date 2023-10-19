n = int(input())
racing_number = input()

tunel = []
matrix = []
kilometers = 0
ci, cj = 0, 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    row = input().split()
    matrix.append(row)

    if len(tunel) < 2:
        for idx in range(n):
            if row[idx] == 'T':
                tunel.append((i, idx))

                if len(tunel) == 2:
                    break

while matrix[ci][cj] != 'F':
    action = input()

    if action == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    di, dj = directions[action]
    ci, cj = ci + di, cj + dj
    kilometers += 10

    if matrix[ci][cj] == 'T':
        matrix[ci][cj] = '.'
        tunel.remove((ci, cj))
        kilometers += 20
        ci, cj = tunel[0]
        matrix[ci][cj] = '.'

else:
    print(f"Racing car {racing_number} finished the stage!")

print(f"Distance covered {kilometers} km.")
matrix[ci][cj] = 'C'
[print(*row, sep='') for row in matrix]
