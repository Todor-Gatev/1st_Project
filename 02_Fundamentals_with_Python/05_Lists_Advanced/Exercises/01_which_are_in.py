# Read user input
first_list = input().split(", ")
second_list = input().split(", ")

# Variables
result = []
# Logic
for substring in first_list:
    for word in second_list:
        if substring in word:
            result.append(substring)
            break
# End of Logic

# Print Output
print(result)
