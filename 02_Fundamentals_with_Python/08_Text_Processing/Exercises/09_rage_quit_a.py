string = input()

new_string = ""
temp_str = ""
unique_symbols = ""
idx = 0
repeats = ""

while idx < len(string):
    ch = string[idx].upper()

    while ch.isdigit():
        repeats += ch
        if idx < len(string) - 1:
            idx += 1
            ch = string[idx].upper()
        else:
            break

    if repeats != "":
        repeats = int(repeats)
        new_string += temp_str * repeats
        repeats = ""
        temp_str = ""

    if ch.isdigit():
        break

    if ch not in unique_symbols:
        unique_symbols += ch

    temp_str += ch
    idx += 1

print(f"Unique symbols used: {len(unique_symbols)}")
print(new_string)
