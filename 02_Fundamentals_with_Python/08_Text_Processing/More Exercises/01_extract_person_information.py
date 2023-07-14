def get_text_between_symbols(string, ch1, ch2):
    result = ""
    is_not_finished = True
    idx = 0
    while is_not_finished:
        if string[idx] == ch1:
            for j in range(idx + 1, len(string)):
                if string[j] == ch2:
                    is_not_finished = False
                    break

                result += string[j]

        idx += 1

    return result


n = int(input())

for _ in range(n):
    text = input()
    name = get_text_between_symbols(text, '@', '|')
    age = get_text_between_symbols(text, '#', '*')

    print(f"{name} is {age} years old.")
