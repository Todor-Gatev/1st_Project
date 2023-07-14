import re

# w{3}\.[A-Za-z0-9]+([-][A-Za-z0-9]+)*(\.[a-z]+)+

regex = re.compile(r"w{3}\.[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[a-z]+)+")

while True:
    row = input()
    if not row:
        break

    result = regex.finditer(row)
    for res in result:
        print(res.group())
