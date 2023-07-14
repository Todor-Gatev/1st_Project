from math import ceil

# Read user input
people = int(input())
capacity = int(input())

# Logic
# if people % capacity != 0:
#     courses = people // capacity + 1
# else:
#     courses = people // capacity
# End of Logic

# Print Output
print(ceil(people / capacity))
