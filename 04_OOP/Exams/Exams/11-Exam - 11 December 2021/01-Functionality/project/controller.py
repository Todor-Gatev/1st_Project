from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []  # Car objects
        self.drivers = []  # Driver objects
        self.races = []  # Race objects

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if next(filter(lambda x: x.model == model, self.cars), None):
            raise f"Car {model} is already created!"

        if car_type not in self.VALID_CAR_TYPES:
            return

        self.cars.append(self.VALID_CAR_TYPES[car_type](model, speed_limit))

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if next(filter(lambda x: x.name == driver_name, self.drivers), None):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if next(filter(lambda x: x.name == race_name, self.races), None):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type not in self.VALID_CAR_TYPES:
            raise Exception(f"Car {car_type} could not be found!")

        for i in range(len(self.cars) - 1, -1, -1):
            if self.cars[i].__class__.__name__ == car_type and not self.cars[i].is_taken:
                car = self.cars[i]
                break
        else:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        car.is_taken = True
        driver.car = car

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)
        driver = next(filter(lambda d: d.name == driver_name, self.drivers), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next(filter(lambda r: r.name == race_name, self.races), None)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted(self.drivers, key=lambda x: -x.car.speed_limit)[:3]
        res = []

        for driver in sorted_drivers:
            driver.number_of_wins += 1
            res.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(res)
