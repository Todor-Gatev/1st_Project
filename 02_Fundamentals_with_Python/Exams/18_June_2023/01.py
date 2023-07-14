# Read user input
num_cities = int(input())
# Variables
total_profit = 0

# Logic
for i in range(1, num_cities + 1):
    name = input()
    income = float(input())
    expenses = float(input())

    if i % 3 == 0:
        if i % 5 != 0:
            expenses += 0.5 * expenses

    if i % 5 == 0:
        income *= 0.9

    profit = income - expenses
    total_profit += profit
    print(f"In {name} Burger Bus earned {profit:.2f} leva.")
# End of Logic

# Print Output
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
