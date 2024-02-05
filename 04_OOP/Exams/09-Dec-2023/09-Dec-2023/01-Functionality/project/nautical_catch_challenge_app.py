from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    # region support methods
    def __get_diver_via_name(self, name) -> BaseDiver:
        return next(filter(lambda d: d.name == name, self.divers), None)

    def __get_fish_via_name(self, name) -> BaseFish:
        return next(filter(lambda f: f.name == name, self.fish_list), None)

    # endregion

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if self.__get_diver_via_name(diver_name):
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self.__get_fish_via_name(fish_name):
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.__get_diver_via_name(diver_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.__get_fish_via_name(fish_name)

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)

                return f"{diver_name} hits a {round(fish.points, 1)}pt. {fish_name}."

            diver.miss(fish.time_to_catch)

            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)

        return f"{diver_name} hits a {round(fish.points, 1)}pt. {fish_name}."

    def health_recovery(self):
        count = 0

        for d in self.divers:
            if d.has_health_issue:
                count += 1
                d.oxygen_level = d.initial_oxygen_level
                d.has_health_issue = False

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.__get_diver_via_name(diver_name)
        res = [
            f"**{diver_name} Catch Report**",
            *[f.fish_details() for f in diver.catch]
        ]

        return "\n".join(res)

    def competition_statistics(self):
        divers_in_statistic = [d for d in self.divers if not d.has_health_issue]
        divers_in_statistic = sorted(divers_in_statistic, key=lambda d: (-d.competition_points, -len(d.catch)))
        res = [
            f"**Nautical Catch Challenge Statistics**",
            *[str(d) for d in divers_in_statistic]
        ]

        return "\n".join(res)

# class BaseDiver(ABC):
#     def __init__(self, name: str, oxygen_level: float):
#         self.name = name
#         self.oxygen_level = oxygen_level
#         self.catch: List[BaseFish] = []
#         self.competition_points = 0.0
#         self.has_health_issue = False
# class BaseFish(ABC):
#     def __init__(self, name: str, points: float, time_to_catch: int):
#         self.name = name
#         self.points = points
#         self.time_to_catch = time_to_catch
