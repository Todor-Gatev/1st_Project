from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPE = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in self.VALID_ASTRONAUT_TYPE:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(self.VALID_ASTRONAUT_TYPE[astronaut_type](name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        p = Planet(name)
        p.items = items.split(", ")
        self.planet_repository.add(p)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_on_mission = self.get_astronauts_for_mission()

        if not astronauts_on_mission:
            raise Exception("You need at least one astronaut to explore the planet!")

        participants = 0

        for astronaut in astronauts_on_mission:
            participants += 1
            for i in range(len(planet.items) - 1, -1, -1):
                # if astronaut.oxygen < astronaut.breathe:
                if astronaut.oxygen <= 0:
                    break

                astronaut.oxygen -= astronaut.breathe
                astronaut.backpack.append(planet.items[i])
                planet.items.pop()
            else:
                break

        if planet.items:
            self.number_of_not_completed_missions += 1

            return "Mission is not completed."

        self.number_of_successful_missions += 1

        return (f"Planet: {planet.name} was explored. "
                f"{participants} astronauts participated in collecting items.")
                # f"{len(astronauts_on_mission)} astronauts participated in collecting items.")

    def report(self):
        return "\n".join([
            f"{self.number_of_successful_missions} successful missions!",
            f"{self.number_of_not_completed_missions} missions were not completed!",
            "Astronauts' info:",
            *[a.get_info() for a in self.astronaut_repository.astronauts],
        ])

    # region supporting staff
    def get_astronauts_for_mission(self):
        a_on_mission = []

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)

        for a in sorted_astronauts:
            if a.oxygen < 30:
                break

            a_on_mission.append(a)

            if len(a_on_mission) == 5:
                break

        return a_on_mission
    # endregion


# a = SpaceStation()
# a.add_astronaut("Geodesist", "G1")
# a.add_astronaut("Geodesist", "G2")
# a.add_astronaut("Geodesist", "G3")
# a.add_astronaut("Geodesist", "G4")
# a.add_astronaut("Meteorologist", "John")
# print(a.report())
# a.recharge_oxygen()
# # print(a.report())
#
# a.add_planet("asd", "a,  , b")
# a.add_planet("asd", "a, b, c, d, e, f, g, h, i, j, k, l, m, n")
# a.add_planet("asd1", "a, b, c, d, e, f, g, h, i, j, k, l, m, n")
# a.add_planet("asd2", "a, b, c, d, e, f, g, h, i, j, k, l, m, n")
#
# print(a.report())
# a.send_on_mission("asd")
# a.send_on_mission("asd")
# a.send_on_mission("asd")
# print(a.report())
#
# for p in a.planet_repository.planets:
#     print(p.items)


# a.add_astronaut("Biologist", "John")
# print(a.retire_astronaut("Johnsff"))
# a.add_astronaut("Biologist", "John1")
# b = SpaceStation()
#
# print(a.report())
# # print(b.astronaut_repository)
