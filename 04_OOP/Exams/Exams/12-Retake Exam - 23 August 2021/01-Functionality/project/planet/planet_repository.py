class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        return next(filter(lambda x: x.name == name, self.planets), None)
