from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_object(self.delicacies, "name", name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.DELICACY_TYPES[type_delicacy](name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_object(self.booths, "booth_number", str(booth_number)):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.BOOTH_TYPES[type_booth](booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)

                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_object(self.booths, "booth_number", str(booth_number))
        delicacy = self.find_object(self.delicacies, "name", delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy.name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_object(self.booths, "booth_number", str(booth_number))
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill
        booth.is_reserved = False
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0

        return (f"Booth {booth_number}:\n"
                f"Bill: {bill:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # region supporting staff
    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion
