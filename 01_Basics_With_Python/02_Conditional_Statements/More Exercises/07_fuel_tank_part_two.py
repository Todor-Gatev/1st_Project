# Read user input
fuel_type = input()
liters_fuel = float(input())
club_card = input()

# Parameters
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

total_price = 0

# Logic
if club_card == 'Yes':
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08

if fuel_type == 'Gasoline':
    total_price = liters_fuel * gasoline_price
elif fuel_type == 'Diesel':
    total_price = liters_fuel * diesel_price
else:
    total_price = liters_fuel * gas_price

if 20 <= liters_fuel <= 25:
    total_price *= 0.92
elif liters_fuel > 25:
    total_price *= 0.90

# End of Logic

# Print Output
print(f'{total_price:.2f} lv.')
