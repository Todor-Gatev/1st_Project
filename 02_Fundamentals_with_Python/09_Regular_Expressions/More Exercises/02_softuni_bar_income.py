import re

income = 0

regex = re.compile(r"%(?P<name>[A-Z][a-z]+)%"
                   r"[^|$%.]*"
                   r"<(?P<product>\w+)>"
                   r"[^|$%.]*"
                   r"\|(?P<qty>\d+)\|"
                   r"[^|$%.]*"
                   r"(?<=[^0-9])(?P<price>\d+(\.\d+)?)\$")

while True:
    info = input()

    if info == "end of shift":
        break

    result = regex.finditer(info)

    for res in result:
        total_price = int(res.group('qty')) * float(res.group('price'))
        income += total_price
        print(f"{res.group('name')}: {res.group('product')} - {total_price:.2f}")

print(f"Total income: {income:.2f}")
