n = int(input())

game_board = []
ig, jg = None, None
amount = 100
is_winning = True
is_jackpot_won = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(n):
    row = list(input())
    game_board.append(row)

    if 'G' in row:
        ig, jg = i, row.index('G')

while True:
    command = input()

    if command == 'end':
        break

    game_board[ig][jg] = '-'
    ig, jg = ig + directions[command][0], jg + directions[command][1]

    if ig not in range(n) or jg not in range(n):
        is_winning = False
        break

    if game_board[ig][jg] == 'W':
        amount += 100
    elif game_board[ig][jg] == 'P':
        amount -= 200

        if amount < 0:
            is_winning = False
            break
    elif game_board[ig][jg] == 'J':
        is_jackpot_won = True
        amount += 100000
        game_board[ig][jg] = 'G'
        break

    game_board[ig][jg] = 'G'

if is_jackpot_won:
    print(f"You win the Jackpot!\n"
          f"End of the game. Total amount: {amount}$")
elif is_winning:
    print(f"End of the game. Total amount: {amount}$")
else:
    print("Game over! You lost everything!")

if is_winning:
    [print(*row, sep='') for row in game_board]
