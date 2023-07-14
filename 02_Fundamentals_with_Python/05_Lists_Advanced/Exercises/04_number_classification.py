# Read user input
int_list = [int(x) for x in input().split(", ")]

# Variables
positive = []
negative = []
even = []
odd = []

# Logic
for num in int_list:
    if num < 0:
        negative.append(str(num))
    else:
        positive.append(str(num))

    if num % 2 == 0:
        even.append(str(num))
    else:
        odd.append(str(num))
# End of Logic

# Print Output
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
