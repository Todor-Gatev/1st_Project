n = int(input())

alice_row, alice_col = None, None
field = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    field.append(input().split())

    if 'A' in field[i]:
        alice_row, alice_col = i, field[i].index('A')
        field[alice_row][alice_col] = '*'

while tea_bags < 10:
    direction = input()
    alice_row, alice_col = alice_row + directions[direction][0], alice_col + directions[direction][1],

    if not (alice_row in range(n) and alice_col in range(n)):
        break

    if field[alice_row][alice_col] == 'R':
        field[alice_row][alice_col] = '*'
        break

    if field[alice_row][alice_col].isdigit():
        tea_bags += int(field[alice_row][alice_col])

    field[alice_row][alice_col] = '*'

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*field[row]) for row in range(n)]
