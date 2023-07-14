# Read user input
quantity = int(input())
days = int(input())

# Variables
budget = 0
total_spirit = 0

# Constant
ornament_set_price = 2
ornament_set_points = 5
skirt_tree_price = 5
skirt_tree_points = 3
garland_tree_price = 3
garland_tree_points = 10
lights_tree_price = 15
lights_tree_points = 17

# Logic
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        budget += ornament_set_price * quantity
        total_spirit += ornament_set_points

    if i % 3 == 0:
        budget += (skirt_tree_price + garland_tree_price) * quantity
        total_spirit += (skirt_tree_points + garland_tree_points)

    if i % 5 == 0:
        budget += lights_tree_price * quantity
        total_spirit += lights_tree_points

    if i % 15 == 0:
        total_spirit += 30

    if i % 10 == 0:
        budget += (lights_tree_price + garland_tree_price + skirt_tree_price)
        total_spirit -= 20


if days % 10 == 0:
    total_spirit -= 30
# End of Logic

# Print Output
print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")
