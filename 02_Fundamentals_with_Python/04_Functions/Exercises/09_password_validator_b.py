def is_valid_password(a):
    errors = []
    if not 6 <= len(a) <= 10:
        errors.append("Password must be between 6 and 10 characters")

    if not a.isalnum():
        errors.append("Password must consist only of letters and digits")

    count = 0
    for char in a:
        if char.isdigit():
            count += 1

            if count > 1:
                break
    else:
        errors.append("Password must have at least 2 digits")

    return errors


# Read user input
user_password = input()

# Logic
errors_list = is_valid_password(user_password)

# Print Output
if errors_list:
    for el in errors_list:
        print(el)
else:
    print("Password is valid")
