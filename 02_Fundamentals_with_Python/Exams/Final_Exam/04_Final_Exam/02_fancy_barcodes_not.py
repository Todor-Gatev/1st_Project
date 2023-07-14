import re

# (@#+(?P<product>[A-Za-z0-9]{6,})@#+,?\s?)+
pattern_line = r"(@#+(?P<product>[A-Za-z0-9]{6,})@#+,?\s?)+"
regex_line = re.compile(pattern_line)
pattern_product = r"@#+(?P<product>[A-Za-z0-9]{6,})@#+"
regex_product = re.compile(pattern_product)
regex_group = re.compile(r"\d+")

for _ in range(int(input())):
    text = input()
    match = regex_line.match(text)

    if match:
        result = regex_product.finditer(text)
        for res in result:
            product = res.group("product")
            groups = regex_group.findall(product)
            if groups:
                product_group = ''.join(groups)
                print(f"Product group: {product_group}")
            else:
                print("Product group: 00")
    else:
        print("Invalid barcode")
