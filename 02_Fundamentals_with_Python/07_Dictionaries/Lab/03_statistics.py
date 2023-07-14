command = input()

products = {}

while command != "statistics":
    product, quantity = command.split(': ')
    quantity = int(quantity)

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

    command = input()

print("Products in stock:")

for product, quantity in products.items():
    print(f"- {product}: {quantity}")

count_all_products = len(products.keys())
sum_all_quantities = sum(products.values())
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")
