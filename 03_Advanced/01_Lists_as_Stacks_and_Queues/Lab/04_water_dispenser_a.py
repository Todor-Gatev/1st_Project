from collections import deque

qty = int(input())

clients = deque()

while True:
    command = input()
    if command == "Start":
        break

    clients.append(command)

while True:
    command = input()
    if command == "End":
        break

    command = command.split()
    if len(command) == 1:
        liters = int(command[0])
        if liters <= qty:
            print(f"{clients.popleft()} got water")
            qty -= liters
        else:
            print(f"{clients[0]} must wait")
            clients.rotate(-1)
    else:
        qty += int(command[1])

print(f"{qty} liters left")
