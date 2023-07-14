# Read user input
offers = input().split(', ')
beggars = int(input())

# Variables
list_beggars = [0] * beggars

# Logic
for idx in range(len(offers)):
    beggar_idx = idx % beggars
    list_beggars[beggar_idx] += int(offers[idx])
# End of Logic

# Print Output
print(list_beggars)
