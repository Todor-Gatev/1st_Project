import re

text = input()

# pattern = r"(^|(?<=\s))(?P<user>[a-z\d]+[\._-]?[a-z\d]+)@(?P<host>[a-z]+[-]?[a-z]+(\.[a-z]+)+)($|(?=[\s\.,]))"
#
# result = re.finditer(pattern, text)
#
# for res in result:
#     # print(f'{res.group("user")}@{res.group("host")}')
#     print(res.group("user") + "@" + res.group("host"))

#  solution 2
pattern = r"(?:^|(?<=\s))[a-z0-9]+(?:[-._][a-z0-9]+)*@[a-z]+(?:-[a-z]+)?(?:\.[a-z]+)+(?:$|(?=[,\s\.]))"
res = re.findall(pattern, text)
print(*res, sep='\n')
