def get_chars_in_range(a, b):
    chars_in_range = ""
    for i in range(ord(a) + 1, ord(b)):
        chars_in_range = chars_in_range + chr(i) + ' '
    return chars_in_range


char1 = input()
char2 = input()

print(get_chars_in_range(char1, char2))
