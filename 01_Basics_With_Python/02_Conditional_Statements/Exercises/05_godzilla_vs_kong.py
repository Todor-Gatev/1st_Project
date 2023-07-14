# Read user input
budget = float(input())
extra_man_number = int(input())
cloth_cost_per_pcs = float(input())

# Logic
cloth_cost = 0
decor = budget * 0.1

if extra_man_number > 150:
    cloth_cost = cloth_cost_per_pcs * extra_man_number * 0.9
else:
    cloth_cost = cloth_cost_per_pcs * extra_man_number

expenses = cloth_cost + decor

# Print Output
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")
