from collections import deque

food_qty = int(input())

orders = deque(int(x) for x in input().split())

if orders:
    print(max(orders))

while orders:
    if food_qty < orders[0]:
        print("Orders left:", *orders)
        break

    food_qty -= orders.popleft()
else:
    print("Orders complete")
