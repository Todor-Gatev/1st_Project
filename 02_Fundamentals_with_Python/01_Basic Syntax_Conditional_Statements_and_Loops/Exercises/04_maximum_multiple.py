# Read user input
divisor = int(input())
boundary = int(input())

# Variables
max_n = 0

# Logic
for i in range(1, boundary+1):
    if i % divisor == 0:
        max_n = i
# End of Logic

# Print Output
print(max_n)
