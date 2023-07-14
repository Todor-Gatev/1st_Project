# Read user input
season = input()
gender = input()
students = int(input())
nights = int(input())

# Parameters

# Variables
discount = 1
price = None
price_per_night = None
sport = None

# Logic
if students >= 50:
    discount = 1 - 0.50
elif students >= 20:
    discount = 1 - 0.15
elif students >= 10:
    discount = 1 - 0.05

if season == 'Winter':
    if gender == 'boys' or gender == 'girls':
        price_per_night = 9.60
        if gender == 'boys':
            sport = 'Judo'
        else:
            sport = 'Gymnastics'
    elif gender == 'mixed':
        price_per_night = 10.00
        sport = 'Ski'
elif season == 'Spring':
    if gender == 'boys' or gender == 'girls':
        price_per_night = 7.20
        if gender == 'boys':
            sport = 'Tennis'
        else:
            sport = 'Athletics'
    elif gender == 'mixed':
        price_per_night = 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if gender == 'boys' or gender == 'girls':
        price_per_night = 15.00
        if gender == 'boys':
            sport = 'Football'
        else:
            sport = 'Volleyball'
    elif gender == 'mixed':
        price_per_night = 20.00
        sport = 'Swimming'

price = price_per_night * nights * students * discount
# End of Logic

# Print Output
print(f"{sport} {price:.2f} lv.")
