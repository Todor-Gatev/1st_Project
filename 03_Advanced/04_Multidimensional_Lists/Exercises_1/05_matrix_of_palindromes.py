from string import ascii_lowercase

chars = list(ascii_lowercase)

rows, columns = [int(x) for x in input().split()]

for i in range(rows):
    for j in range(columns):
        text = chars[i] + chars[j + i] + chars[i]
        print(text, end=' ')

    print()
