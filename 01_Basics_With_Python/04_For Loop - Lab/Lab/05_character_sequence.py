# Read user input
input_text = input()

# Logic
for i in input_text:
    print(i)

# test

input_text = "Soft"
for i in input_text:
    print(i)             # S o f t  in a column
for i in "Soft":
    print(i)             # S o f t  in a column
for i in "Soft":
    print(i, end="")     # Soft  in a row
