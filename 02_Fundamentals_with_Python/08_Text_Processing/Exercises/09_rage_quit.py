text = input()

unique = ""
part_rag = ""
rag = ""

for i in range(len(text)):
    ch = text[i]
    if i == (len(text) - 1):
        ch1 = 'a'
    else:
        ch1 = text[i + 1]

    if ch.isdigit():
        if ch1.isdigit():
            rag += part_rag.upper() * int(ch + ch1)
            part_rag = ""
            continue
        else:
            rag += part_rag.upper() * int(ch)
            part_rag = ""
            continue

    if ch.lower() not in unique:
        unique += ch.lower()

    part_rag += ch

print(f"Unique symbols used: {len(unique)}")
print(rag)
