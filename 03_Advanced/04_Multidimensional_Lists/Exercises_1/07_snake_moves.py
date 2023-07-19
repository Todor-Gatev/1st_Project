from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = input()

matrix = []
counter = -1

for row in range(rows):
    matrix.append(deque())
    for column in range(columns):
        counter += 1
        ch = counter % len(snake)
        if row % 2 == 0:
            matrix[row].append(snake[ch])
        else:
            matrix[row].appendleft(snake[ch])

[print(f"{''.join(matrix[row])}") for row in range(rows)]

# solution 2
# snake = list(input())
# chars = deque(snake)
#
# for row in range(rows):
#     while len(chars) < columns:
#         chars.extend(snake)
#
#     if row % 2 == 0:
#         print(*[chars.popleft() for _ in range(columns)], sep='')
#     else:
#         print(*[chars.popleft() for _ in range(columns)][::-1], sep='')
