from collections import deque

quantity_of_the_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if quantity_of_the_food < orders[0]:
        print("Orders left: ", end='')
        print(*orders)
        exit()

    quantity_of_the_food -= orders.popleft()

print("Orders complete")
