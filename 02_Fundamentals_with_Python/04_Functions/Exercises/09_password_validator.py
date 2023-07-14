def is_length_correct(a):
    return 6 <= len(a) <= 10


def is_only_letters_and_digits(a):
    return a.isalnum()


def does_have_two_digits(a):
    count = 0
    for char in a:
        if char.isdigit():
            count += 1
            
            if count > 1:
                return True

    return False


# def is_valid(a)
user_password = input()
is_valid = True

if not is_length_correct(user_password):
    print("Password must be between 6 and 10 characters")
    is_valid = False

if not is_only_letters_and_digits(user_password):
    print("Password must consist only of letters and digits")
    is_valid = False


if not does_have_two_digits(user_password):
    print("Password must have at least 2 digits")
    is_valid = False


if is_valid:
    print("Password is valid")
