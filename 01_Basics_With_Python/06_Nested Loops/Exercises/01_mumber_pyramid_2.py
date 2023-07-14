# Read user input
n = int(input())

# Variables
current = 1
is_current_bigger_than_n = False
letter = 'a'

# Logic
for row in range(1, n + 1):
    if is_current_bigger_than_n:
        break
    for column in range(1, row + 1):
        if current > n:
            is_current_bigger_than_n = True
            break

        # print(f'{current}', end=' ')
        print(f'{letter}', end=' ')
        current += 1
    print()
# End of Logic
