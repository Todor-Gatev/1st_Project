from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    DRINK_TYPES = {"Tea": Tea, "Water": Water}
    TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    # region getters and setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() is None:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    # endregion

    # region supporting staff
    def __get_food_via_name(self, name: str):
        return next(filter(lambda x: x.name == name, self.food_menu), None)

    def __get_drink_via_name(self, name: str):
        return next(filter(lambda x: x.name == name, self.drinks_menu), None)

    def __get_table_via_table_number(self, table_number):
        return next(filter(lambda x: x.table_number == table_number, self.tables_repository), None)

    # endregion

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in self.FOOD_TYPES:
            return

        if self.__get_food_via_name(name):
            raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(self.FOOD_TYPES[food_type](name, price))

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in self.DRINK_TYPES:
            return

        if self.__get_drink_via_name(name):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(self.DRINK_TYPES[drink_type](name, portion, brand))

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in self.TABLE_TYPES:
            return

        if self.__get_table_via_table_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(self.TABLE_TYPES[table_type](table_number, capacity))

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)

                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__get_table_via_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered_food = []
        food_not_in_menu = []

        for food_name in food_names:
            food = self.__get_food_via_name(food_name)

            if food:
                table.order_food(food)
                ordered_food.append(food)
                # self.total_income += food.price
            else:
                food_not_in_menu.append(food_name)

        res = [
            f"Table {table_number} ordered:",
            *[repr(f) for f in ordered_food],
            f"{self.name} does not have in the menu:",
            *food_not_in_menu
        ]

        return "\n".join(res)

    def order_drink(self, table_number: int, *drinks_names):
        table = self.__get_table_via_table_number(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        drinks_not_in_menu = []

        for drink_name in drinks_names:
            drink = self.__get_drink_via_name(drink_name)

            if drink:
                table.order_drink(drink)
                ordered_drinks.append(drink)
                # self.total_income += drink.price
            else:
                drinks_not_in_menu.append(drink_name)

        res = [
            f"Table {table_number} ordered:",
            *[repr(f) for f in ordered_drinks],
            f"{self.name} does not have in the menu:",
            *drinks_not_in_menu
        ]

        return "\n".join(res)

    def leave_table(self, table_number: int):
        table = self.__get_table_via_table_number(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return (f"Table: {table_number}\n"
                f"Bill: {bill:.2f}")

    def get_free_tables_info(self):
        return "\n".join(t.free_table_info() for t in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
