from collections import deque

clients = deque()

while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        while clients:
            print(clients.popleft())
    else:
        clients.append(command)

print(f"{len(clients)} people remaining.")
