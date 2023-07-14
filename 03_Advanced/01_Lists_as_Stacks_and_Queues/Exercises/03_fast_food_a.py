from collections import deque

qty = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

while orders:
    if qty < orders[0]:
        print("Orders left: ", end='')
        print(*orders)
        exit()

    qty -= orders.popleft()

print("Orders complete")
