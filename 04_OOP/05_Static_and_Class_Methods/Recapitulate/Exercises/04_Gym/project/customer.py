from project.next_id_mixin import NextIdMixin


class Customer(NextIdMixin):
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

# a = Customer("a", "f", "d")
# a1 = Customer("a", "f", "d")
# a2 = Customer("a", "f", "d")
#
# print(a.id)
# print(a1.id)
# print(a2.id)
# print(Customer.id)
