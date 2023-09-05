from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

# print(repo.find("az"))
# print(repo.add(food))
# print(repo.products)
# print(repr(repo))
# print(repo.remove("az"))
# print(repr(repo))
# print(repo.remove("apple"))
# print(repr(repo))
# print(type(repo.find("water")))
