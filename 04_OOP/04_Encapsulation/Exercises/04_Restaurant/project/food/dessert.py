from project.food.food import Food


class Dessert(Food):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, Dessert.PRICE, Dessert.GRAMS)
