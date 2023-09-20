from project.next_id_mixin import NextIdMixin


class Equipment(NextIdMixin):
    id = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    #     Equipment.id += 1
    #
    # @staticmethod
    # def get_next_id():
    #     return Equipment.id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


# e1 = Equipment("eq1")
# e2 = Equipment("eq2")
# e3 = Equipment("eq3")
#
# print(e1)
# print(e2)
# print(e3)
#
# e1 = Equipment("eq1")
# print(e1)
