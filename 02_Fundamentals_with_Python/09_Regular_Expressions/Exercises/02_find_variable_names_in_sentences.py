import re

pattern = r"(^|(?<=\s))\_{1}(?P<id>[A-Za-z]+)($|(?=\s))"
text = input()

result = re.finditer(pattern, text)
id_list = []

for res in result:
    # print(res.group(), end='')
    id_list.append(res.group("id"))

print(*id_list, sep=',')
