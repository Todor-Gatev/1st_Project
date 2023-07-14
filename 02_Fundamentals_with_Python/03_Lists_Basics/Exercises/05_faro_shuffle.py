# Read user input
initial = input().split()
num_shuffles = int(input())

# Variables
shuffled = []

# Logic
for _ in range(num_shuffles):
    shuffled = []
    first_half = []
    second_half = []
    for i in range(len(initial)):
        if i < int(len(initial) / 2):
            first_half.append(initial[i])
        else:
            second_half.append(initial[i])

    for i in range(int(len(initial) / 2)):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])

    initial = shuffled
# End of Logic

# Print Output
print(shuffled)
