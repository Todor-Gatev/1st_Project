from project.product import Product


class Food(Product):
    def __int__(self, name: str, quantity: int):
        super().__init__(name, 15)
