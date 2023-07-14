import re

text = ""
while True:
    row = input()
    if row:
        # text += row
        text = row
        result = re.finditer(r"\d+", text)
        for res in result:
            print(res.group(), end=' ')
        # result = re.findall(r"\d+", text)
        # if result:
        #     print(*result, sep=' ', end=' ')
    else:
        break

# result = re.findall(r"\d+", text)
# print(*result, sep=' ')
#
# result = re.finditer(r"\d+", text)
# for res in result:
#     print(res.group(), end=' ')
