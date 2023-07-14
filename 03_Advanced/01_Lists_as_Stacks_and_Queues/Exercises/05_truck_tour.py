pumps = int(input())
available_fuel = 0
pump_idx = 0

for idx in range(pumps):
    litters, distance = [int(x) for x in input().split()]
    available_fuel += litters
    if available_fuel >= distance:
        available_fuel -= distance
        continue

    pump_idx = idx + 1
    available_fuel = 0

print(pump_idx)
