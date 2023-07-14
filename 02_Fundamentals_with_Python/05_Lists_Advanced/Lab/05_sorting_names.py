def sort_words(list_a):
    # list_a.sort()
    # list_a.sort(key=lambda x: -len(x))
    list_a.sort(key=lambda x: (-len(x), x))


# Read user input
names = input().split(", ")

# Variables

# Logic
sorted_names = sorted(names, key=lambda x: (-len(x), x))
# sorted_names = sorted(names, key=lambda x: (x, -len(x)))  # it's different to above
# names.sort(key=lambda x: (-len(x), x))
# sort_words(names)
# End of Logic

# Print Output
# print(names)
print(sorted_names)
