import re

command = input()

# r"%(?P<name>[A-Z][a-z]+)%[^%\.\|\$]*<(?P<product>\w+)>[^%\.\|\$]*
# \|(?P<count>\d+)\|[^%\.\|\$]*(?<!\d)(?P<price>\d+(\.\d+)?)\$"
pattern = r"%(?P<name>[A-Z][a-z]+)%" \
          r"[^%\.\|\$]*" \
          r"<(?P<product>\w+)>" \
          r"[^%\.\|\$]*" \
          r"\|(?P<count>\d+)\|" \
          r"[^%\.\|\$]*" \
          r"(?<!\d)(?P<price>\d+(\.\d+)?)\$"
regex = re.compile(pattern)

income = 0

while command != "end of shift":
    # if not regex.search(command):
    #     command = input()
    #     continue

    result = regex.finditer(command)
    for res in result:
        name = res.group("name")
        product = res.group("product")
        qty = int(res.group("count"))
        price = float(res.group("price"))
        income += qty * price
        print(f"{name}: {product} - {qty * price:.2f}")

    command = input()

print(f"Total income: {income:.2f}")
