# Read user input
factor = int(input())
count = int(input())

# Variables
result = []

# Logic
for i in range(1, count + 1):
    result.append(i * factor)
# End of Logic

# Print Output
print(result)

# print(result, sep='-*')
# print(2, 3, 4, 11, 23, sep='-*')
