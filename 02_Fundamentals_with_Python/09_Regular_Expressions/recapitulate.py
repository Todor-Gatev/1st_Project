import re

info = input()

title = re.findall(r"<title>(.+)</title>", info)
rough_content = ''.join(re.findall(r"<body(>.+<)/body>", info))
rough_content = re.findall(r">([^<]+)", rough_content)
content = ''.join(rough_content)
content = content.replace("\\n", '')

print(f"Title: {title[0]}")
print(f"Content: {content}")
