import re

text = input()

pattern = r"(?:^|(?<=\s))\-?(?:[0]|[1-9]\d*)(?:\.\d+)?(?:$|(?=\s))"
res = re.findall(pattern, text)
print(*res)


# pattern = r"(?:^|(?<=\s))(-?)([0]|[1-9][0-9]*)(\.\d+)?(?:$|(?=\s))"
# # text = input()
# text = "1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5"
#
# result = re.finditer(pattern, text)
# for res in result:
#     print(res.group(), end=' ')

# print()
# result = re.match(pattern, text)
# print(result)
# print(result.groupdict())
# for res in result:  # Error
#     # print(res)
#     print(res.group(), end=' ')

# result = re.findall(pattern, text)
# for res in result:
#     print(res[0], res[1], res[2], end=' ')
# print()
# for res in result:
#     print(res, end=' ')
# print()
# print(result)
# print(*result)
