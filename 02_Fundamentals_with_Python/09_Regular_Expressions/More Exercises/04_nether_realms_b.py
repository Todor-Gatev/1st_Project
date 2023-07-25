import re

names = input().split(',')

demon_book = {}

for name in names:
    name = name.strip()
    health = sum([ord(ch) for ch in re.findall(r"[^0-9*./+\-]", name)])
    damage = sum([float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", name)])
    operators = re.findall(r"[*/]", name)

    for operator in operators:
        if operator == '*':
            damage *= 2
        else:
            damage /= 2

    demon_book[name] = [health, damage]

demon_book = dict(sorted(demon_book.items()))

for name, info in demon_book.items():
    print(f"{name} - {info[0]} health, {info[1]:.2f} damage")
