cars = {}

for _ in range(int(input())):
    car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split('|')]
    cars[car] = [mileage, fuel]

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split(" : ")
    action, car = command[0], command[1],

    if action == "Drive":
        distance, fuel = int(command[2]), int(command[3]),

        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            cars[car][0] += distance
            cars[car][1] -= fuel

            if cars[car][0] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif action == "Refuel":
        fuel = int(command[2])
        fuel_in_tank = cars[car][1]

        if fuel + fuel_in_tank > 75:
            fuel = 75 - fuel_in_tank
            cars[car][1] = 75
        else:
            cars[car][1] += fuel

        print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        revert_km = int(command[2])
        car_km = cars[car][0]

        if car_km - revert_km < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= revert_km
            print(f"{car} mileage decreased by {revert_km} kilometers")

for car, info in cars.items():
    mileage, fuel = info[0], info[1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
