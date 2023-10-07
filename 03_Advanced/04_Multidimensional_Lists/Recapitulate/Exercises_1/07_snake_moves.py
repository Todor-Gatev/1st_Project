from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = list(input())
chars = deque(snake)

for row in range(rows):
    while len(chars) < columns:
        chars.extend(snake)

    if row % 2 == 0:
        print(*[chars.popleft() for _ in range(columns)], sep='')
    else:
        print(*[chars.popleft() for _ in range(columns)][::-1], sep='')

# solution 2
# rows, cols = [int(x) for x in input().split()]
# snake = input()
#
# temp_snake = snake
#
# for i in range(rows):
#     while len(temp_snake) < cols:
#         temp_snake += snake
#
#     row = temp_snake[:cols]
#     temp_snake = temp_snake[cols:]
#
#     if i % 2 == 0:
#         print(row)
#     else:
#         print(row[::-1])
