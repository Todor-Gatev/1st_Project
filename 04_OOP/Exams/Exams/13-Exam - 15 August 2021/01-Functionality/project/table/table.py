from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    # region getters and setters
    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not self.min_table_number() <= value <= self.max_table_number():
            raise ValueError(self.table_number_error_message())

        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    # endregion

    # region abstract methods
    @abstractmethod
    def min_table_number(self):
        ...

    @abstractmethod
    def max_table_number(self):
        ...

    @abstractmethod
    def table_number_error_message(self):
        ...
    # endregion

    def reserve(self, number_of_people: int):
        if not self.is_reserved and number_of_people <= self.capacity:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food):
        self.food_orders.append(baked_food)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.is_reserved = False
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return (f"Table: {self.table_number}\n"
                    f"Type: {self.__class__.__name__}\n"
                    f"Capacity: {self.capacity}")

