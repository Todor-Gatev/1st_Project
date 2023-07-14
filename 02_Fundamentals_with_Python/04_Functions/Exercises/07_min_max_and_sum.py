# Read user input
user_list = [int(x) for x in input().split()]

# Logic
minimum_number = min(user_list)
maximum_number = max(user_list)
sum_of_all_numbers = sum(user_list)

# Print Output
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")
