parking_lot = set()

for _ in range(int(input())):
    direction, number = input().split(", ")

    if direction == "IN":
        parking_lot.add(number)
    elif direction == "OUT":
        parking_lot.remove(number)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")
