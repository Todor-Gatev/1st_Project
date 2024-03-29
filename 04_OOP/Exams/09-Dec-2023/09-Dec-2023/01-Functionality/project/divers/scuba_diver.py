from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, self.initial_oxygen_level)

    @property
    def initial_oxygen_level(self):
        return 540

    def miss(self, time_to_catch: int):
        self.oxygen_level = max(0, self.oxygen_level - round(time_to_catch * 0.3))

        if self.oxygen_level == 0:
            self.has_health_issue = True
