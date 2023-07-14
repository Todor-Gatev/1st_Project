class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        result = ""
        if species == "mammal":
            species = species.capitalize() + 's'
            result = f"{species} in {self.name}: {', '.join(self.mammals)}"

        result += f"\nTotal animals: {self.__animals}"
        return result


zoo_name = input()
n = int(input())

zoo = Zoo(zoo_name)

for _ in range(n):
    species1, name1 = input().split()
    zoo.add_animal(species1, name1)

species1 = input()

print(zoo.get_info(species1))
