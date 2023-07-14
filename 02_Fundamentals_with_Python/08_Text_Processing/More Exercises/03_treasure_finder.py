# from math import ceil


def get_text_between_symbols(string_f, ch1, ch2):
    result = ""
    is_not_finished = True
    idx1 = 0
    while is_not_finished:
        sym = string_f[idx1]
        if sym == ch1:
            for j in range(idx1 + 1, len(string_f)):
                if string_f[j] == ch2:
                    is_not_finished = False
                    break

                result += string_f[j]

        idx1 += 1

    return result


key = [int(x) for x in input().split()]

message = input()

while message != "find":
    decoded = ""
    # if len(message) > len(key):
    #     diff = ceil(len(message) / len(key))
    #     key *= diff

    for idx in range(len(message)):
        idx_key = idx % len(key)
        ch = message[idx]
        new_ch = chr(ord(ch) - key[idx_key])
        decoded += new_ch

    treasure_type = get_text_between_symbols(decoded, '&', '&')
    coordinates1 = get_text_between_symbols(decoded, '<', '>')
    print(f"Found {treasure_type} at {coordinates1}")
    message = input()
