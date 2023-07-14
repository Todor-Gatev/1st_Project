from collections import deque

litters = int(input())

people = deque()

while True:
    name = input()
    if name == "Start":
        break

    people.append(name)

while True:
    command = input()
    if command == "End":
        break

    data = command.split()
    if len(data) == 1:
        wanted_litters = int(data[0])
        if litters >= wanted_litters:
            litters -= wanted_litters
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    else:
        litters += int(data[1])

print(f"{litters} liters left")
