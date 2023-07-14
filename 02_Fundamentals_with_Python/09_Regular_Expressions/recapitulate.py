import re

html = input()

title = re.findall(r"(?<=<title>).+(?=</title>)", html)

rough_content = re.findall(r"(?<=<body).+(?=/body>)", html)[0]
rough_content = re.findall(r"(?<=>)[^<]+", rough_content)
rough_content = ''.join(rough_content)
content = rough_content.replace("\\n", '')

print(f"Title: {title[0]}")
print(f"Content: {content}")
