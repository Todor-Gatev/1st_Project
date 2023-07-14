import re

furniture_lst = []
total_cost = 0
# p = r"^>{2}(?P<name>.+)<{2}(?P<price>\d+(\.\d+)?)!(?P<qty>\d+)$"
regex = re.compile(r"^>{2}"
                   r"(?P<name>[A-Za-z]+)"
                   r"<{2}"
                   r"(?P<price>\d+(\.\d+)?)"
                   r"!"
                   r"(?P<qty>\d+?)$")

while True:
    command = input()
    if command == "Purchase":
        break

    if not regex.search(command):
        continue

    result = regex.finditer(command)
    for res in result:
        furniture_lst.append(res.group("name"))
        price = float(res.group("price"))
        qty = int(res.group("qty"))
        total_cost += price * qty

print("Bought furniture:")
if furniture_lst:
    print(*furniture_lst, sep='\n')
print(f"Total money spend: {total_cost:.2f}")
