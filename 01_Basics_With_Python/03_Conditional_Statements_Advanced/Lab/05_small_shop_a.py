# Read user input
product = input()
city = input()
quantity = float(input())

# Parameters

# Variables
coffee_price = 0
water_price = 0
beer_price = 0
sweets_price = 0
peanuts_price = 0

price = 0
is_invalid_city_or_product = False

# Logic
if city == 'Sofia':
    coffee_price = 0.50
    water_price = 0.80
    beer_price = 1.20
    sweets_price = 1.45
    peanuts_price = 1.60
elif city == 'Plovdiv':
    coffee_price = 0.40
    water_price = 0.70
    beer_price = 1.15
    sweets_price = 1.30
    peanuts_price = 1.50
elif city == 'Varna':
    coffee_price = 0.45
    water_price = 0.70
    beer_price = 01.10
    sweets_price = 01.35
    peanuts_price = 1.55
else:
    is_invalid_city_or_product = True

if product == "coffee":
    price = quantity * coffee_price
elif product == "water":
    price = quantity * water_price
elif product == "beer":
    price = quantity * beer_price
elif product == "sweets":
    price = quantity * sweets_price
elif product == "peanuts":
    price = quantity * peanuts_price
else:
    is_invalid_city_or_product = True

# End of Logic

# Print Output
if is_invalid_city_or_product:
    print('Error')
else:
    print(price)
