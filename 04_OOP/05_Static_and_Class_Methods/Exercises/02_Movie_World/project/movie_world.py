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

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = None
        customer = None
        # region finding customer and dvd region
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
                break

        for c in self.customers:
            if c.id == customer_id:
                customer = c
                break
        # endregion

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            return f"DVD is already rented"

