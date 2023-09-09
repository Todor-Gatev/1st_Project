class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    # region getters and setters
    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #     pass

    @property
    def price(self):
        return self.__price

    # @price.setter
    # def price(self, value):
    #     pass
    # endregion


# p = Product("asd", 3)
# print(p.name)

