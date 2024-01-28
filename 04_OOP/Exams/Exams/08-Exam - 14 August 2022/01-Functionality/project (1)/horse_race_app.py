from typing import Type

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []  # horse obj
        self.jockeys = []  # jockeys obj
        self.horse_races = []  # horse_races obj

    # region supporting staff
    def __get_horse_by_name(self, name):
        return next(filter(lambda x: x.name == name, self.horses), None)

    def __get_jockey_by_name(self, name):
        return next(filter(lambda x: x.name == name, self.jockeys), None)

    def __get_horse_race_by_race_type(self, race_type):
        return next(filter(lambda x: x.race_type == race_type, self.horse_races), None)

    @staticmethod
    def __is_horse_race(horse_race, race_type) -> (None, str):
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

    # endregion

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> (None, str, Type[Exception]):
        if self.__get_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in self.HORSE_TYPES:
            return

        self.horses.append(self.HORSE_TYPES[horse_type](horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        if self.__get_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        if self.__get_horse_race_by_race_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> (str, Type[Exception]):
        jockey = self.__get_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for i in range(len(self.horses) - 1, -1, -1):
            if (not self.horses[i].is_taken) and self.horses[i].__class__.__name__ == horse_type:
                horse = self.horses[i]
                break
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> (str, Type[Exception]):
        horse_race = self.__get_horse_race_by_race_type(race_type)

        self.__is_horse_race(horse_race, race_type)

        jockey = self.__get_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> (str, Type[Exception]):
        horse_race = self.__get_horse_race_by_race_type(race_type)

        self.__is_horse_race(horse_race, race_type)

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        horse = None
        jockey = None
        max_speed = 0

        for j in horse_race.jockeys:
            if j.horse.speed > max_speed:
                jockey = j
                horse = j.horse
                max_speed = j.horse.speed

        return (f"The winner of the {race_type} race, "
                f"with a speed of {horse.speed}km/h "
                f"is {jockey.name}! "
                f"Winner's horse: {horse.name}.")
