def price_calc(product_type, quantity):
    result = None

    if product_type == "coffee":
        result = quantity * 1.50
    elif product_type == "water":
        result = quantity * 1.00
    elif product_type == "coke":
        result = quantity * 1.40
    elif product_type == "snacks":
        result = quantity * 2.00

    return result


prod_type = input()
qty = int(input())

print(f"{price_calc(prod_type, qty):.2f}")
