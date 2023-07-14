target = float(input())

income = 0
is_party = False

while income < target:
    cocktail = input()

    if cocktail == 'Party!':
        is_party = True
        break

    pcs = int(input())
    price = pcs * len(cocktail)

    if price % 2 != 0:
        price *= 1 - 0.25

    income += price

if is_party:
    print(f'We need {(target - income):.2f} leva more.')
else:
    print("Target acquired.")

print(f'Club income - {income:.2f} leva.')
