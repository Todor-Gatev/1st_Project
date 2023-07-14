# Read user input
budget = int(input())
season = input()
fishermen = int(input())

# Logic
rent = 0
discount = 0

if season == "Spring":
    rent = 3000
elif season == "Summer":
    rent = 4200
elif season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishermen <= 6:
    discount = 0.1
elif fishermen <= 11:
    discount = 0.15
else:
    discount = 0.25

price = rent * (1 - discount)

if fishermen % 2 == 0 and season != "Autumn":
    price *= 0.95

# Print Output
diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
