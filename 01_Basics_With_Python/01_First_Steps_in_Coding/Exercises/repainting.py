
nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.50
paint_price = paint * 1.1 * 14.50
thinner_price = thinner * 5.00
material_price = nylon_price + paint_price + thinner_price + 0.40
hourly_rate = material_price * 0.3

total_price = hourly_rate * hours + material_price
print(total_price)
