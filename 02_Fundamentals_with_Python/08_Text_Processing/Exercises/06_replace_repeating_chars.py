text = input()

new_text = text[0]

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        continue

    new_text += text[i]

print(new_text)
