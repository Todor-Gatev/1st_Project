import re

barcode_regex = re.compile(r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+")
group_regex = re.compile(r"\d+")

for _ in range(int(input())):
    text = input()

    barcode_lst = barcode_regex.findall(text)

    if barcode_lst:
        barcode = barcode_lst[0]
        group = group_regex.findall(barcode)

        if group:
            print(f"Product group: {''.join(group)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
