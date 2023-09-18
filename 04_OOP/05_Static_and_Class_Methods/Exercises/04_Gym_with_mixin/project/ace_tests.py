from project.customer import Customer
from project.equipment import Equipment

c1 = Customer("ala1", "vd1", "ljf")
c2 = Customer("ala2", "vd2", "ljf2")
c3 = Customer("ala3", "vd3", "ljf3")

print(c1)
print(c2)
print(c3)
c1 = Customer("ala1", "vd1", "ljf")
print(c1)

e1 = Equipment("eq1")
e2 = Equipment("eq2")
e3 = Equipment("eq3")

print(e1)
print(e2)
print(e3)
e3 = Equipment("eq3")
print(e3)
