from math import ceil

# Read user input
magnolias_number = int(input())
hyacinths_number = int(input())
rouses_number = int(input())
cacti_number = int(input())
gift_price = float(input())

# Parameters
magnolias_price = 3.25
hyacinths_price = 4.00
rouses_price = 3.50
cacti_price = 8.00

income = 0.95 * (magnolias_price * magnolias_number
                 + hyacinths_price * hyacinths_number
                 + rouses_price * rouses_number
                 + cacti_price * cacti_number)

diff_money = income - gift_price

# Logic
if diff_money >= 0:
    print(f'She is left with {int(diff_money)} leva.')
else:
    print(f'She will have to borrow {ceil(-diff_money)} leva.')
# End of Logic

# Print Output
