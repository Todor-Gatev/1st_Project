import re

total_cost = 0
furniture = []
regex = re.compile(r">{2}(?P<name>[A-Za-z]+)<{2}(?P<price>0|[1-9]\d*(\.\d+)?)!(?P<qty>\d+)")

while True:
    info = input()

    if info == "Purchase":
        break

    result = regex.search(info)

    if result:
        name = result.group("name")
        price = float(result.group("price"))
        qty = int(result.group("qty"))
        total_cost += price * qty
        furniture.append(name)

print("Bought furniture:")
print(*furniture, sep='\n') if furniture else None
print(f"Total money spend: {total_cost:.2f}")
