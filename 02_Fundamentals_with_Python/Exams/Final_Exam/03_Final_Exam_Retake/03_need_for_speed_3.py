cars = {}

for _ in range(int(input())):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")
    action = command[0]
    car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            cars[car][0] += distance
            cars[car][1] -= fuel

        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    elif action == "Refuel":
        fuel = int(command[2])
        if cars[car][1] + fuel > 75:
            fuel = 75 - cars[car][1]
            cars[car][1] = 75
            print(f"{car} refueled with {fuel} liters")
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        kilometers = int(command[2])
        if cars[car][0] - kilometers < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car, value in cars.items():
    print(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
