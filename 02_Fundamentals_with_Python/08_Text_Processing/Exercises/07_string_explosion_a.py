text = input().split('>')
print(text)
result = [text[0]]
text.pop(0)
left_force = 0

for el in text:
    force = int(el[0]) + left_force
    if force > len(el):
        result.append('')
        left_force = force - len(el)
    else:
        result.append(el[force:])
        left_force = 0

print('>'.join(result))
