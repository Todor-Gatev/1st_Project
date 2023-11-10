from project.car.car import Car


class SportsCar(Car):
    # region getters and setters
    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not 400 <= value <= 600:
            raise ValueError(f"Invalid speed limit! Must be between {400} and {600}!")

        self.__speed_limit = value
    # endregion
