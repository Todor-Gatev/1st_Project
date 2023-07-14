# Read user input
str_one = input()
str_two = input()

# Logic
for i in range(len(str_two)):
    if str_one[i] == str_two[i]:
        continue

    for j in range(len(str_one)):
        if i >= j:
            print(str_two[j], end='')
        else:
            print(str_one[j], end='')
    print()
# End of Logic
