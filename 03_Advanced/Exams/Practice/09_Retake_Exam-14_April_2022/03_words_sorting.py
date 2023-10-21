def words_sorting(*args):
    sum_of_values = 0
    words = {}
    result = None

    for word in args:
        value = 0

        for ch in list(word):
            value += ord(ch)

        words[word] = value
        sum_of_values += value

    if sum_of_values % 2 == 0:
        result = sorted(words.items())
    else:
        result = sorted(words.items(), key=lambda x: -x[1])

    return "\n".join(f"{k} - {v}" for k, v in result)


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#     ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
