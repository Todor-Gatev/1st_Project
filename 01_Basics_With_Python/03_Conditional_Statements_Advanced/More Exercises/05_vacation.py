# Read user input
budget = float(input())
season = input()

# Parameters

# Variables
location = ''
accommodation = ''
price = ''

# Logic
if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = 0.65 * budget
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.45 * budget
elif budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = 0.80 * budget
    elif season == 'Winter':
        location = 'Morocco'
        price = 0.60 * budget
else:
    accommodation = 'Hotel'
    price = 0.90 * budget
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
# End of Logic

# Print Output
print(f"{location} – {accommodation} – {price:.2f}")
