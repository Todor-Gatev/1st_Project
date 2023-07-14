# Read user input
age = float(input())
gender = input()

# Logic
if gender == "m":
    if age < 16:
        print("Master")
    else:
        print("Mr.")
else:
    if age < 16:
        print("Miss")
    else:
        print("Ms.")
