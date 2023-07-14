def is_char_in_chars(f_list):
    if len(f_list) > 0:
        return True
    else:
        return False


# Read user input
string = input()

# Variables
chars = []
take_list = []
skip_list = []
idx = 0
result = ""

# Logic
for ch in string:
    if ch.isdigit():
        if idx % 2 == 0:
            take_list.append(int(ch))
        else:
            skip_list.append(int(ch))

        idx += 1
    else:
        chars.append(ch)


for i in range(len(take_list)):
    if not is_char_in_chars(chars):
        break

    for _ in range(take_list[i]):
        if not is_char_in_chars(chars):
            break

        result += chars[0]
        chars.pop(0)

    for _ in range(skip_list[i]):
        if not is_char_in_chars(chars):
            break

        chars.pop(0)
# End of Logic

# Print Output
print(result)
