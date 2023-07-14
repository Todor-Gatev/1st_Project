n = int(input())

word = input()
string_list = []
list_of_string_containing_word = []

for _ in range(n):
    current_string = input()
    # string_list.extend(current_string)
    string_list.append(current_string)

    if word in current_string:
        list_of_string_containing_word.append(current_string)

print(string_list)
print(list_of_string_containing_word)
