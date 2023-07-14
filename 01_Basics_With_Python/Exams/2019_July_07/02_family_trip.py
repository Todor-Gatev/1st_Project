budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_add_expenses = int(input())

if nights > 7:
    price_per_night *= 0.95

add_expenses = budget * percent_add_expenses / 100
price = nights * price_per_night + add_expenses

diff = budget - price
if diff >= 0:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{-diff:.2f} leva needed.')
