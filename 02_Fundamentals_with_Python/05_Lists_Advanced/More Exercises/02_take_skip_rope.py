# Read user input
string = input()

# Variables
char_list = []
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
        char_list.append(ch)

is_char_in_char_list = True

for i in range(len(take_list)):
    if not is_char_in_char_list:
        break

    for _ in range(take_list[i]):
        if len(char_list) == 0:
            is_char_in_char_list = False
            break
        result += char_list[0]
        char_list.pop(0)

    for _ in range(skip_list[i]):
        if len(char_list) == 0:
            is_char_in_char_list = False
            break
        char_list.pop(0)
# End of Logic

# Print Output
print(result)
