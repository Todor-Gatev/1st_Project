sub_str = input()
text = input()

while sub_str in text:
    text = text.replace(sub_str, '')

print(text)
