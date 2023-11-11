from project.car.car import Car


class MuscleCar(Car):
    # region getters and setters
    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not 250 <= value <= 450:
            raise ValueError(f"Invalid speed limit! Must be between {250} and {450}!")

        self.__speed_limit = value

    # endregion
