# Read user input
a = int(input())
b = int(input())
c = int(input())

# Variables
max_num = None
# Logic
if a >= b:
    max_num = a
else:
    max_num = b

if c > max_num:
    max_num = c
# End of Logic

# Print Output
print(max_num)
