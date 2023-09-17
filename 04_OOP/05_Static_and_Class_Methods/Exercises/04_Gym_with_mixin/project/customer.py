from project.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

        # Customer.id += 1
    #
    # @staticmethod
    # def get_next_id():
    #     return Customer.id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


# c = Customer("ala", "vd", "ljf")
# c1 = Customer("ala2", "vd2", "ljf2")
#
# print(c)
# print(c1)
