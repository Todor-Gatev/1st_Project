from math import ceil

# Read user input
people = int(input())
entrance_price = float(input())
chair_price = float(input())
umbrella_price = float(input())

# Logic
umbrellas = ceil(people / 2)
chairs = ceil(people * 0.75)
price = people * entrance_price + \
        umbrellas * umbrella_price + \
        chairs * chair_price
# End of Logic

# Print Output
print(f'{price:.2f} lv.')
