cars = set()

for _ in range(int(input())):
    action, number = input().split(", ")
    if action == "IN":
        cars.add(number)
    elif action == "OUT":
        cars.remove(number)

if cars:
    print(*cars, sep='\n')
else:
    print("Parking Lot is Empty")
