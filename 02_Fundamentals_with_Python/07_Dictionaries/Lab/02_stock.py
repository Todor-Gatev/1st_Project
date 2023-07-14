data = input().split()
searched_product = input().split()

products = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

for product in searched_product:
    if product in products.keys():
        quantity = products[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
