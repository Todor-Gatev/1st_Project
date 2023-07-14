# Variables
coffee_count = 0

# Logic
while True:
    text = input()

    if text == "END":
        break

    if text == "coding" or text == "dog" or text == "cat" or text == "movie":
        coffee_count += 1
    elif text == "CODING" or text == "DOG" or text == "CAT" or text == "MOVIE":
        coffee_count += 2

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

# End of Logic
