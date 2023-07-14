winner = None
best_score = 0

while True:
    user_name = input()

    if user_name == 'Stop':
        break

    score = 0

    for char in user_name:
        user_num = int(input())

        if user_num == ord(char):
            score += 10
        else:
            score += 2

    if score >= best_score:
        winner = user_name
        best_score = score

print(f'The winner is {winner} with {best_score} points!')
