# Read user input
offers = input().split(', ')
beggars = int(input())

# Variables
list_beggars = [0] * beggars
offer_idx = 0

# Logic
for offer in offers:
    idx = offer_idx % beggars
    list_beggars[idx] += int(offer)
    offer_idx += 1
# End of Logic

# Print Output
print(list_beggars)
