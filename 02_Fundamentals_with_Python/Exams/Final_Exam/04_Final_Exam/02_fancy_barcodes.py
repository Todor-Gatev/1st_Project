import re

pattern_product = r"^@#+(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
regex_product = re.compile(pattern_product)
regex_group = re.compile(r"\d+")

for _ in range(int(input())):
    text = input()
    match = regex_product.match(text)

    if match:
        product = match.group("product")
        group = regex_group.findall(product)
        if group:
            product_group = ''.join(group)
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
