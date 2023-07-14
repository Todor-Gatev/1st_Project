# Read user input
season = input()
km_per_month = float(input())

# Parameters

# Variables
salary = 0

# Logic
if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        salary = 0.75 * km_per_month
    elif season == 'Summer':
        salary = 0.90 * km_per_month
    elif season == 'Winter':
        salary = 1.05 * km_per_month
elif km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        salary = 0.95 * km_per_month
    elif season == 'Summer':
        salary = 1.10 * km_per_month
    elif season == 'Winter':
        salary = 1.25 * km_per_month
elif km_per_month <= 20000:
    salary = 1.45 * km_per_month

salary *= 0.90 * 4
# End of Logic

# Print Output
print(f'{salary:.2f}')
