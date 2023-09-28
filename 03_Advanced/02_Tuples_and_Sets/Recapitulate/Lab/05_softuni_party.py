guests = set()

for _ in range(int(input())):
    guests.add(input())

guests = list(guests)

while True:
    guest_num = input()

    if guest_num == "END":
        break

    guests.remove(guest_num)

guests.sort()

print(len(guests))
print(*guests, sep="\n")
