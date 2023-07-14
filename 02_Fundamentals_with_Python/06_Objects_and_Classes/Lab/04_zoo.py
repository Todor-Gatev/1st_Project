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
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}" \
                   f"\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}" \
                   f"\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}" \
                   f"\nTotal animals: {self.__animals}"


# Read user input
zoo = Zoo(input())
num = int(input())

# Variables

# Logic
for _ in range(num):
    species1, name1 = input().split()
    zoo.add_animal(species1, name1)
# End of Logic

# Print Output
print(zoo.get_info(input()))
