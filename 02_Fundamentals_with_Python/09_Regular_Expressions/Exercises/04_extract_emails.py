import re

text = input()

pattern = r"(^|(?<=\s))(?P<user>[a-z\d]+[\._-]?[a-z\d]+)@(?P<host>[a-z]+[-]?[a-z]+(\.[a-z]+)+)($|(?=[\s\.,]))"

result = re.finditer(pattern, text)

for res in result:
    # print(f'{res.group("user")}@{res.group("host")}')
    print(res.group("user") + "@" + res.group("host"))
