text = input()

for i in range(len(text)):
    if text[i] == ':':
        print(text[i] + text[i + 1])


# text = input().split(':')
#
# for i in range(1, len(text)):
#     if text[i] == '':
#         text[i + 1] = ':' + text[i + 1]
#         continue
#     emoticon = ':' + text[i][0]
#     print(emoticon)
