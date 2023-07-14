# Read user input
first_list = input().split(", ")
second_str = input()

# Variables
result = []
# Logic
for substring in first_list:
    if substring in second_str:
        result.append(substring)
# End of Logic

# Print Output
print(result)
