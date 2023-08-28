from project.animal import Animal


class Lion(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 50)


# lion = Lion("alf", "male", 12)
# print(lion.money_for_care)
# lion.money_for_care = 78
# print(lion.money_for_care)

