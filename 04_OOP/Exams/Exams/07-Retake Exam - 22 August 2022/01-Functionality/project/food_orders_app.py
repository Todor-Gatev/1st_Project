from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if self.__find_object(self.clients_list, "phone_number", client_phone_number):
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        self.__is_menu_ready()

        return "\n".join(m.details() for m in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__is_menu_ready()

        if not self.__find_object(self.clients_list, "phone_number", client_phone_number):
            self.register_client(client_phone_number)
            # client = Client(client_phone_number)
            # self.clients_list.append(client)

        client = self.__find_object(self.clients_list, "phone_number", client_phone_number)

        for meal_name, qty in meal_names_and_quantities.items():
            meal = self.__find_object(self.menu, "name", meal_name)

            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal.quantity < qty:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, qty in meal_names_and_quantities.items():
            meal = self.__find_object(self.menu, "name", meal_name)
            client.shopping_cart.append(meal)
            client.ordered_meals[meal_name] = client.ordered_meals.get(meal_name, 0) + qty
            meal.quantity -= qty
            client.bill += meal.price * qty

        meal_names = ", ".join(m.name for m in client.shopping_cart)

        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_object(self.clients_list, "phone_number", client_phone_number)
        self.__is_ordered_meals(client)

        for meal_name, qty in client.ordered_meals.items():
            meal = self.__find_object(self.menu, "name", meal_name)
            meal.quantity += qty

        client.shopping_cart.clear()
        client.ordered_meals.clear()
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_object(self.clients_list, "phone_number", client_phone_number)
        self.__is_ordered_meals(client)
        self.receipt_id += 1
        result = (f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f}"
                  f" was successfully paid for {client_phone_number}.")

        client.shopping_cart.clear()
        client.ordered_meals.clear()
        client.bill = 0.0

        return result

    def __str__(self):
        return (f"Food Orders App has {len(self.menu)} meals on the menu"
                f" and {len(self.clients_list)} clients.")

    # region supporting staff
    @staticmethod
    def __is_ordered_meals(client):
        if not client.bill:
            raise Exception("There are no ordered meals!")

    def __is_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def __find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    @staticmethod
    def __get_objects(collection: list, attribute: str, value: str):
        return [obj for obj in collection if str(getattr(obj, attribute)) == value]
    # endregion
