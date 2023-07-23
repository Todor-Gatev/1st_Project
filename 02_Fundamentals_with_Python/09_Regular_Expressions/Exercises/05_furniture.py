import re

furniture = []
total_cost = 0
# p = r"^>{2}(?P<name>.+)<{2}(?P<price>\d+(\.\d+)?)!(?P<qty>\d+)$"
regex = re.compile(r"^>{2}"
                   r"(?P<name>[A-Za-z]+)"
                   r"<{2}"
                   r"(?P<price>\d+(\.\d+)?)"
                   r"!"
                   r"(?P<qty>\d+?)$")

# while True:
#     command = input()

#     if command == "Purchase":
#         break
#
#     if not regex.search(command):
#         continue
#
#     result = regex.finditer(command)
#     for res in result:
#         furniture_lst.append(res.group("name"))
#         price = float(res.group("price"))
#         qty = int(res.group("qty"))
#         total_cost += price * qty

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
