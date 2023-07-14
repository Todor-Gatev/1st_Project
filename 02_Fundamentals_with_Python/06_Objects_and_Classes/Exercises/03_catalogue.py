class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.f_list = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        for el in self.products:
            if el[0] == first_letter:
                self.f_list.append(el)

        return self.f_list

    def __repr__(self):
        self.products.sort()

        return f"Items in the {self.name} catalogue:\n" + '\n'.join(self.products)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
