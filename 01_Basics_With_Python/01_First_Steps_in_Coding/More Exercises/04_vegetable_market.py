# Read user input
vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

bgn_to_eur = 1 / 1.94

# Logic
bgn_income = (vegetable_price * vegetable_kg) + (fruit_price * fruit_kg)

eur_income = bgn_income * bgn_to_eur
# End of Logic

# Print Output
print(f'{eur_income:.2f}')
