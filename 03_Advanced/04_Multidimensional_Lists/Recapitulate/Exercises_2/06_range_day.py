n = 5

training_field = []
left_targets = 0
targets_out = []
r, c = None, None
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    training_field.append(input().split())
    left_targets += training_field[i].count('x')

    if 'A' in training_field[i]:
        r, c = i, training_field[i].index('A')

for _ in range(int(input())):
    if left_targets == 0:
        break

    action, direction, *info = [int(x) if x.isdigit() else x for x in input().split()]
    di, dj = directions[direction]

    if action == "shoot":
        i, j = r + di, c + dj

        while i in range(n) and j in range(n):
            if training_field[i][j] == 'x':
                training_field[i][j] = '.'
                left_targets -= 1
                targets_out.append([i, j])
                break
            else:
                i, j = i + di, j + dj

    elif action == "move":
        steps = int(info[0])

        for s in range(steps, 0, -1):
            i, j = r + di * s, c + dj * s

            if i in range(n) and j in range(n) and training_field[i][j] == '.':
                r, c = i, j
                break

if left_targets:
    print(f"Training not completed! {left_targets} targets left.")
else:
    print(f"Training completed! All {len(targets_out)} targets hit.")

print(*targets_out, sep='\n')
