# Read user input
fuel_type = input()
liters_available = float(input())

# Parameters

# Logic
if fuel_type != 'Diesel' \
        and fuel_type != 'Gasoline' \
        and fuel_type != 'Gas':
    print('Invalid fuel!')
elif liters_available >= 25:
    print(f'You have enough {fuel_type.lower()}.')
else:
    print(f'Fill your tank with {fuel_type.lower()}!')
# End of Logic

# Print Output
