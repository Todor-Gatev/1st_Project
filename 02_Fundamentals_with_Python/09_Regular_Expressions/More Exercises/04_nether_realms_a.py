import re

demons = input().split(",")
info_demons = {}

for demon in demons:
    demon = demon.strip()
    health_list = re.findall(r"[^\d+*/.-]", demon)
    health = sum([ord(ch) for ch in health_list])
    # damage = 0
    # result = re.finditer(r"-?(?<![\d.])(0|[1-9]\d*)(\.\d+)?(?=\D)", demon)
    # result = re.finditer(r"-?[0-9]+(?:\.[0-9]+)?", demon)
    damage_list = re.findall(r"-?[0-9]+(?:\.[0-9]+)?", demon)
    damage = sum(map(float, damage_list))
    # for res in result:
    #     damage += float(res.group())

    result = re.findall(r"[*/]", demon)

    for ch in result:
        if ch == '*':
            damage *= 2
        elif ch == '/':
            damage /= 2

    info_demons[demon] = [health, damage]

info_demons = dict(sorted(info_demons.items()))

for demon, values, in info_demons.items():
    print(f"{demon} - {values[0]} health, {values[1]:.2f} damage")
#
# for el in sorted(info_demons.items()):
#     print(f"{el[0]} - {el[1][0]} health, {el[1][0]:.2f} damage")
