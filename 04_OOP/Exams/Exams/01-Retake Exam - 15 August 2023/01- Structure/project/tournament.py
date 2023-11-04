from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")

        new_equipment = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise ValueError("Invalid team type!")

        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."

        new_team = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)

        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = [t for t in self.teams if t.name == team_name][0]
        equipment = [e for e in self.equipment if e.__class__.__name__ == equipment_type][-1]

        if team.budget < equipment.price:
            raise ValueError("Budget is not enough!")

