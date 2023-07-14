# Read user input
n = int(input())
word = input()

str_list = []
# str_word_list = []

# Logic
for _ in range(n):
    tmp_str = input()
    str_list.append(tmp_str)

print(str_list)

for el in str_list:
    if word not in el:
        str_list.remove(el) # Be very careful with remove in for cycle!!!
        # str_word_list.append(el)
# End of Logic

print(str_list)
# print(str_word_list)

# Be very careful with remove!!!
# it's not working with the following input!!

# 7
# SoftUni
# I study at SoftUni
# I walk to work
# I learn Python at SoftUni
# I walk to work
# I walk to work
# I learn Python at SoftUni
# I learn Python at SoftUni
