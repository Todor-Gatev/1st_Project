# Read user input
n = int(input())

# Parameters
water_tank_capacity = 255

# Variables
litters_in_tank = 0

# Logic
for _ in range(n):
    litters_flow = int(input())
    litters_in_tank += litters_flow

    if litters_in_tank > water_tank_capacity:
        litters_in_tank -= litters_flow
        print("Insufficient capacity!")
# End of Logic

# Print Output
print(litters_in_tank)
