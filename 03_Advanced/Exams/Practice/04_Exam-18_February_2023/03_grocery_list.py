def shop_from_grocery_list(budget: int, products: list, *info):
    for el in info:
        if not products:
            break

        if el[0] in products:
            if budget < el[1]:
                break

            budget -= el[1]
            products.remove(el[0])

    if not products:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(products)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

