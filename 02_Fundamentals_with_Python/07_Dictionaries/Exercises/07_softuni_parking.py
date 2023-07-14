n = int(input())

parking = {}

for _ in range(n):
    data = input().split()
    registered = data[0]
    name = data[1]

    if registered == "register":
        license_plate = data[2]

        if name not in parking:
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif registered == "unregister":
        if name in parking:
            parking.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, license_plate in parking.items():
    print(f"{name} => {license_plate}")
