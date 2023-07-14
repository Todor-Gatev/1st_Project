# Read user input
x_one = int(input())
y_one = int(input())
x_two = int(input())
y_two = int(input())
x = int(input())
y = int(input())

# Parameters

# Variables
is_on_border = False

# Logic
if x == x_one or x == x_two:
    if y_one <= y <= y_two:
        is_on_border = True
elif y == y_one or y == y_two:
    if x_one <= x <= x_two:
        is_on_border = True

# End of Logic

# Print Output
if is_on_border:
    print('Border')
else:
    print('Inside / Outside')
