class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        return next(filter(lambda x: x.name == name, self.astronauts), None)
