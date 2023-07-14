# Read user input
input_deck = input().split()
count_of_faro_shuffles = int(input())

result_deck = []

# Logic
for _ in range(count_of_faro_shuffles):
    first_half_deck = input_deck[:len(input_deck) // 2]
    second_half_deck = input_deck[len(input_deck) // 2:]
    result_deck = []

    for i in range(len(first_half_deck)):
        result_deck.append(first_half_deck[i])
        result_deck.append(second_half_deck[i])

    input_deck = result_deck
# End of Logic

# Print Output
print(result_deck)
