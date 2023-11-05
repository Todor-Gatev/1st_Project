from typing import List

from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPE = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAM_TYPE = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[KneePad, ElbowPad] = []
        self.teams: List[IndoorTeam, OutdoorTeam] = []

    # region getters and setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError()

        self.__capacity = value

    # endregion

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT_TYPE:
            raise Exception("Invalid equipment type!")

        self.equipment.append(self.VALID_EQUIPMENT_TYPE[equipment_type]())

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPE:
            raise Exception("Invalid team type!")

        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."

        self.teams.append(self.VALID_TEAM_TYPE[team_type](team_name, country, advantage))

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self.get_objects(self.equipment, "EQUIPMENT_TYPE", equipment_type)[-1]
        team = self.find_object(self.teams, "name", team_name)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        team.equipment.append(equipment)
        team.budget -= equipment.price
        self.equipment.remove(equipment)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self.find_object(self.teams, "name", team_name)

        if not team:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)

        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment = self.get_objects(self.equipment, "EQUIPMENT_TYPE", equipment_type)
        [e.increase_price() for e in equipment]

        return f"Successfully changed {len(equipment)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self.find_object(self.teams, "name", team_name1)
        team2 = self.find_object(self.teams, "name", team_name2)

        if not team1.TEAM_TYPE == team2.TEAM_TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_res = team1.advantage + sum(p.protection for p in team1.equipment)
        team2_res = team2.advantage + sum(p.protection for p in team2.equipment)

        if team1_res == team2_res:
            return "No winner in this game."

        if team1_res > team2_res:
            team1.win()
            return f"The winner is {team1.name}."

        team2.win()

        return f"The winner is {team2.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:",
                  *[t.get_statistics() for t in sorted_teams]]

        return "\n".join(result)

    # supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
