from typing import List


class Book:
    def __init__(self, name):
        self.name = name


b1, b2, b3 = Book("a"),  Book("b"),  Book("c")


class Customer:
    id = 1

    def __init__(self):
        self.id = Customer.id
        self.books: List[Book] = [b1, b2, b3]

    @staticmethod
    def find_object(collection: list, attribute: str, value: str):
        for obj in collection:
            if str(getattr(obj, attribute)) == value:
                return obj

    def find_book(self, book_name):
        b = self.find_object(self.books, "name", book_name)

        if b:
            return b

        return "no book"
        # try:
        #     return [b for b in self.books if b.name == book_name][0]
        # except IndexError:
        #     return "no book"


c1 = Customer()
print(c1.find_book('d'))

# c1 = Customer()
# print(c1.id)  # 1
# Customer.id = 2  # instances created before this row will have one class variable value,
# # and after this row other class variable(data attribute) value
# c2 = Customer()
# print(c1.id)  # 1
# print(c2.id)  # 2
# print(Customer.id)  # 2
