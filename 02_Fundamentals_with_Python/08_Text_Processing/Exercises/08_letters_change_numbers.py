from string import ascii_lowercase, ascii_uppercase


def get_result(last_letter1, result1):
    if last_letter1.isupper():
        subtract = 1 + ascii_uppercase.find(last_letter)
        result1 -= subtract
    elif last_letter1.lower():
        add = 1 + ascii_lowercase.find(last_letter)
        result1 += add

    return result1


str_list = input().split()

total_sum = 0

for text in str_list:
    num = int(text[1:-1])
    first_letter = text[0]
    last_letter = text[-1]
    if first_letter.isupper():
        divider = 1 + ascii_uppercase.find(first_letter)
        result = num / divider
        # if last_letter.isupper():
        #     subtract = 1 + ascii_uppercase.find(last_letter)
        #     result -= subtract
        # elif last_letter.lower():
        #     add = 1 + ascii_lowercase.find(last_letter)
        #     result += add

        total_sum += get_result(last_letter, result)
    elif first_letter.lower():
        multiplier = 1 + ascii_lowercase.find(first_letter)
        result = num * multiplier
        # if last_letter.isupper():
        #     subtract = 1 + ascii_uppercase.find(last_letter)
        #     result -= subtract
        # elif last_letter.lower():
        #     add = 1 + ascii_lowercase.find(last_letter)
        #     result += add

        total_sum += get_result(last_letter, result)

print(f"{total_sum:.2f}")
