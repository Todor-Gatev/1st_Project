import re

names = input().split(",")
data = {}


health_regex = re.compile(r"[^\d+.*\-/\s]")
damage_regex = re.compile(r"-?[0-9]+(?:\.[0-9]+)?")
operator_regex = re.compile(r"[/*]")

for name in names:
    health_ch_list = health_regex.findall(name)
    health = 0
    for ch in health_ch_list:
        health += ord(ch)

    damage_list = damage_regex.findall(name)
    damage = sum([float(x) for x in damage_list])

    operator_list = operator_regex.findall(name)
    for operator in operator_list:
        if operator == '*':
            damage *= 2
        else:
            damage /= 2

    data[name.strip()] = [health, damage]

data = dict(sorted(data.items()))

for key, value in data.items():
    print(f"{key} - {value[0]} health, {value[1]:.2f} damage")
