drink = input()
sugar = input()
pcs = int(input())

discount = 1
discount_one = 1

if sugar == 'Without':
    discount = 1 - 0.35

if drink == 'Espresso' and pcs >= 5:
    discount_one = 1 - 0.25

price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = pcs * discount * discount_one * 0.90
    elif sugar == 'Normal':
        price = pcs * discount * discount_one * 1.00
    elif sugar == 'Extra':
        price = pcs * discount * discount_one * 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = pcs * discount * discount_one * 1.00
    elif sugar == 'Normal':
        price = pcs * discount * discount_one * 1.20
    elif sugar == 'Extra':
        price = pcs * discount * discount_one * 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price = pcs * discount * discount_one * 0.50
    elif sugar == 'Normal':
        price = pcs * discount * discount_one * 0.60
    elif sugar == 'Extra':
        price = pcs * discount * discount_one * 0.70

if price > 15:
    price *= 1 - 0.20

print(f"You bought {pcs} cups of {drink} for {price:.2f} lv.")
