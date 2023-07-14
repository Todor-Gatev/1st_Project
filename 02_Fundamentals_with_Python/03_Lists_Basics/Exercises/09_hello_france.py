# Read user input
collection_of_items = input().split('|')
budget = float(input())

# Parameters
train_ticket_costs = 150
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50

markup = 1.4

# Variables
new_prices_float = []
left_money = budget

# Logic

for el in collection_of_items:
    item_details = el.split("->")

    if item_details[0] == "Clothes" and \
            float(item_details[1]) <= clothes_max_price and \
            float(item_details[1]) <= left_money:
        left_money -= float(item_details[1])
        new_prices_float.append(float(item_details[1]) * markup)
    elif item_details[0] == "Shoes" and \
            float(item_details[1]) <= shoes_max_price and \
            float(item_details[1]) <= left_money:
        left_money -= float(item_details[1])
        new_prices_float.append((float(item_details[1]) * markup))
    elif item_details[0] == "Accessories" and \
            float(item_details[1]) <= accessories_max_price and \
            float(item_details[1]) <= left_money:
        left_money -= float(item_details[1])
        new_prices_float.append(float(item_details[1]) * markup)

profit = sum(new_prices_float) - (budget - left_money)
available_money = sum(new_prices_float) + left_money
# End of Logic

# Print Output
print(' '.join(f"{x:.2f}" for x in new_prices_float))
print(f"Profit: {profit:.2f}")

if available_money >= train_ticket_costs:
    print("Hello, France!")
else:
    print("Not enough money.")
