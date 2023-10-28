class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])


first_pizza = Pizza.pepperoni()
print(first_pizza.ingredients)  # ['tomato sauce', 'parmesan', 'pepperoni']
