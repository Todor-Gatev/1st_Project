from string import ascii_lowercase, ascii_uppercase


def get_position(f_string, ch):
    return f_string.find(ch) + 1


strings = input().split()

total_sum = 0

for string in strings:
    num = int(string[1:-1])
    ch1 = string[0]
    ch_end = string[-1]

    if ch1.isupper():
        num /= get_position(ascii_uppercase, ch1)
    else:
        num *= get_position(ascii_lowercase, ch1)

    if ch_end.isupper():
        num -= get_position(ascii_uppercase, ch_end)
    else:
        num += get_position(ascii_lowercase, ch_end)

    total_sum += num

print(f"{total_sum:.2f}")
