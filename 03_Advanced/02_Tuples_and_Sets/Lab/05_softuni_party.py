guests = set()

for _ in range(int(input())):
    guests.add(input())

while True:
    command = input()

    if command == "END":
        break

    guests.remove(command)

guests = list(guests)

guests.sort()

print(len(guests))
print(*guests, sep='\n')
