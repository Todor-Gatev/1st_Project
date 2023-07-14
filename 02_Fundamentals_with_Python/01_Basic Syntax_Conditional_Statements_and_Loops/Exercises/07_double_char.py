# Logic
while True:
    text = input()

    if text == "End":
        break

    if text == "SoftUni":
        continue

    for char in text:
        for i in range(2):
            print(char, end="")

    print()
# End of Logic
