def return_characters_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=' ')


# Read user input
char1 = input()
char2 = input()

# Print Output
return_characters_in_range(char1, char2)

#
# def return_characters_in_range(ch1, ch2):
#     chr_in_range_list = []
#     for i in range(ord(ch1) + 1, ord(ch2)):
#         chr_in_range_list.append(chr(i))
#
#     return chr_in_range_list
#
#
# # Read user input
# char1 = input()
# char2 = input()
#
# # Print Output
# result = return_characters_in_range(char1, char2)
# print(' '.join(result))


# def get_chars_in_range(a, b):
#
#     pass

#
# a = input()
# b = input()
# char_lst = []
# chars_in_range = ""
# for i in range(ord(a) + 1, ord(b)):
#     char_lst.append(chr(i))
#     chars_in_range = chars_in_range + chr(i) + ' '
#
# print(chars_in_range)
# char1 = input()
# char2 = input()
