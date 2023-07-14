import re

text = input()

title = re.findall(r"<title>(?P<title>.+)</title>", text)
print("Title: ", end='')
print(*title)

rough_content = re.findall(r"<body>(.*)</body>", text)[0]
rough_content = '>' + rough_content + '<'
content = ""
result = re.finditer(r">(?P<part_of_title>[^<]+)", rough_content)

for res in result:
    content += res.group("part_of_title")

content = content.replace("\\n", '')
print(f"Content: {content}")
