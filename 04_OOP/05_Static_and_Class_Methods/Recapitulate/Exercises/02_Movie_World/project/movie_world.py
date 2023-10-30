from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        c = self.find_object(self.customers, "id", str(customer_id))
        d = self.find_object(self.dvds, "id", str(dvd_id))

        if d in c.rented_dvds:
            return f"{c.name} has already rented {d.name}"

        if d.is_rented:
            return "DVD is already rented"

        if d.age_restriction > c.age:
            return f"{c.name} should be at least {d.age_restriction} to rent this movie"

        d.is_rented = True
        c.rented_dvds.append(d)

        return f"{c.name} has successfully rented {d.name}"

    def __repr__(self) -> str:
        return "\n".join(str(x) for x in [*self.customers, *self.dvds])
