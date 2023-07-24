import re

# regex = re.compile(r"w{3}\.[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[a-z]+)+")
regex = re.compile(r"w{3}\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?:\.[a-z]+)+")

while True:
    text = input()

    if not text:
        break

    # result = regex.finditer(text)
    #
    # for res in result:
    #     print(res.group())

    result = regex.findall(text)

    if result:
        print(*result, sep="\n")
