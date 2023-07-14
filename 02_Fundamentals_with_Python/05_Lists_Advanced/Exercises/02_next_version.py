# Read user input
current_version_list = input().split('.')

# Variables

# Logic
int_current_version = int(''.join(current_version_list))
str_next_version = str(int_current_version + 1)
next_version_list = list(str_next_version)
result = '.'.join(next_version_list)
# End of Logic

# Print Output
print(result)
