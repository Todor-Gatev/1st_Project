# Read user input
km = int(input())
time_of_the_day = input()

# Parameters
taxi_initial_price = 0.70
taxi_day_price = 0.79
taxi_night_price = 0.90
bus_price = 0.09
train_price = 0.06
price = 0

# Logic
if km >= 100:
    price = km * train_price
elif km >= 20:
    price = km * bus_price
elif time_of_the_day == 'day':
    price = km * taxi_day_price + taxi_initial_price
else:
    price = km * taxi_night_price + taxi_initial_price

# End of Logic

# Print Output
print(f'{price:.02f}')
