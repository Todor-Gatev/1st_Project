# Read user input
budget = float(input())
season = input()

# Parameters

# Variables
price = 0
class_car = ''
type_car = ''

# Logic
if budget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = 0.35 * budget
    elif season == 'Winter':
        type_car = 'Jeep'
        price = 0.65 * budget
elif budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        type_car = 'Cabrio'
        price = 0.45 * budget
    elif season == 'Winter':
        type_car = 'Jeep'
        price = 0.80 * budget
else:
    class_car = 'Luxury class'
    type_car = 'Jeep'
    price = 0.90 * budget
# End of Logic

# Print Output
print(f"{class_car}")
print(f"{type_car} - {price:.2f}")
