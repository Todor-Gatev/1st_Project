from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_HORSES:
            return

        if self.find_object(self.horses, "name", horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        self.horses.append(self.VALID_HORSES[horse_type](horse_name, horse_speed))

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_object(self.jockeys, "name", jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_object(self.horse_races, "race_type", race_type):
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_object(self.jockeys, "name", jockey_name)
        horse = None

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for h in reversed(self.horses):
            if h.HORSE_TYPE == horse_type:
                if not h.is_taken:
                    horse = h
                    break
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self.find_object(self.horse_races, "race_type", race_type)
        jockey = self.find_object(self.jockeys, "name", jockey_name)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self.find_object(self.horse_races, "race_type", race_type)

        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockey = None
        max_speed = 0

        for j in horse_race.jockeys:
            if j.horse.speed > max_speed:
                jockey = j
                max_speed = j.horse.speed

        return (f"The winner of the {race_type} race, with a speed of {max_speed}km/h is {jockey.name}! "
                f"Winner's horse: {jockey.horse.name}.")

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion
