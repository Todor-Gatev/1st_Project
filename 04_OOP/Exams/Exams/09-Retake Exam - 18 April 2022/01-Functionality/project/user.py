class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    # region getters and setters
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    # endregion

    def __str__(self):
        res = [
            f"Username: {self.username}, Age: {self.age}",
            "Liked movies:" if self.movies_liked else "Liked movies:\nNo movies liked.",
            *[m.details() for m in self.movies_liked],
            "Owned movies:" if self.movies_owned else "Owned movies:\nNo movies owned.",
            *[m.details() for m in self.movies_owned]
        ]

        return "\n".join(res)
