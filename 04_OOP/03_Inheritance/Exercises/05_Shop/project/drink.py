from project.product import Product


class Drink(Product):
    def __int__(self, name: str, quantity: int):
        super().__init__(name, 10)
