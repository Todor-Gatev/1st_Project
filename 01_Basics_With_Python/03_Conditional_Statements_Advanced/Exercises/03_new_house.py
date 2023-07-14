# Read user input
flower_name = input()
pcs_flowers = int(input())
budget = int(input())

# Logic
price = 0
if flower_name == "Roses":
    if pcs_flowers > 80:
        price = 5.00 * 0.9
    else:
        price = 5.00
elif flower_name == "Dahlias":
    if pcs_flowers > 90:
        price = 3.80 * 0.85
    else:
        price = 3.80
elif flower_name == "Tulips":
    if pcs_flowers > 80:
        price = 2.80 * 0.85
    else:
        price = 2.80
elif flower_name == "Narcissus":
    if pcs_flowers < 120:
        price = 3.00 * 1.15
    else:
        price = 3.00
elif flower_name == "Gladiolus":
    if pcs_flowers < 80:
        price = 2.50 * 1.2
    else:
        price = 2.50

total_price = pcs_flowers * price
diff = abs(budget - total_price)

# Print Output
if budget >= total_price:
    print(f"Hey, you have a great garden "
          f"with {pcs_flowers} {flower_name} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
