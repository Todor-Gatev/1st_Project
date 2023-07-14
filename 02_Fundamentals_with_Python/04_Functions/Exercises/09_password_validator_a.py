def is_password_valid(text):
    is_valid = True
    digit_counter = 0

    if len(text) < 6 or 10 < len(text):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not text.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    for ch in text:
        if ch.isdigit():
            digit_counter += 1

            if digit_counter > 1:
                break
    else:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


# Read user input
user_pass = input()

# Logic


# Print Output
if is_password_valid(user_pass):
    print("Password is valid")
