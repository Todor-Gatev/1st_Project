# Read user input
string = input()

# Variables
chars = ""
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
        chars += ch


for i in range(len(take_list)):
    if not chars:
        break

    end_idx = min(take_list[i], len(chars))
    result += chars[:end_idx]
    chars = chars[end_idx:]

    end_idx = min(skip_list[i], len(chars))
    chars = chars[end_idx:]
# End of Logic

# Print Output
print(result)
