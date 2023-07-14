from collections import deque

queue = deque()

while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        while queue:
            print(queue.popleft())

        continue

    queue.append(command)

print(f"{len(queue)} people remaining.")
