class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_long_enough = len(value) > 7
        is_upper_char = [x for x in value if x.isupper()]
        is_digit_in_password = [x for x in value if x.isdigit()]

        # if is_digit_in_password and is_long_enough and is_upper_char:
        #     self.__password = value
        # else:
        #     raise ValueError("The password must be 8 or more characters"
        #                      " with at least 1 digit and 1 uppercase letter.")

        if not is_digit_in_password or not is_long_enough or not is_upper_char:
            raise ValueError("The password must be 8 or more characters"
                             " with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

    # def __repr__(self):
    #     return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
#
profile_with_invalid_username = Profile('Too_long_username', 'Any')

# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

# wrong_username = Profile("User", "Passw0rd")
# print(wrong_username)

# wrong_password = Profile("Usernmasdfa", "Pas")
# print(wrong_password)
