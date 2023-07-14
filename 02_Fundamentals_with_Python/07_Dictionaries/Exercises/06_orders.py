data = input()

orders = {}

while data != "buy":
    name, price, qty = data.split()
    price = float(price)
    qty = int(qty)

    if name not in orders:
        orders[name] = [0.0, 0]

    orders[name][0] = price
    orders[name][1] += qty

    data = input()

for name, values in orders.items():
    total_price = values[0] * values[1]
    print(f"{name} -> {total_price:.2f}")
