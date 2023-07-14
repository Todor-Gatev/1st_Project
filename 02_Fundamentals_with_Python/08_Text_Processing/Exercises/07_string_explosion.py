text = input()

i = 0

while i < len(text):
    if text[i] == '>':
        z = i + 1
        x = int(text[z])

        while x and z < len(text):
            if text[z] != '>':
                text = text[:z] + text[z + 1:]
                x -= 1
            else:
                z += 1
                i += 1
                x += int(text[z])

    i += 1

print(text)
