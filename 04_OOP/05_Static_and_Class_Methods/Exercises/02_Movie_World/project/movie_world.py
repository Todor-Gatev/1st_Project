from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def find_instance_via_id(collection: list, id_num: int):
        for result in collection:
            if result.id == id_num:
                return result

    # @staticmethod
    # def find_object(collection: list, attribute: str, value: int):
    #     for obj in collection:
    #         if getattr(obj, attribute) == value:
    #             return obj

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_instance_via_id(self.customers, customer_id)
        dvd = self.find_instance_via_id(self.dvds, dvd_id)
        # region finding customer and dvd
        # for d in self.dvds:
        #     if d.id == dvd_id:
        #         dvd = d
        #         break
        #
        # for c in self.customers:
        #     if c.id == customer_id:
        #         customer = c
        #         break
        # endregion

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_instance_via_id(self.customers, customer_id)
        dvd = self.find_instance_via_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        # customers_info = "\n".join(str(c) for c in self.customers)
        # dvd_info = "\n".join(str(d) for d in self.dvds)
        # return f"{customers_info}\n{dvd_info}"

        # return "\n".join([*[str(c) for c in self.customers], *[str(d) for d in self.dvds]])

        return "\n".join(str(x) for x in [*self.customers, *self.dvds])
