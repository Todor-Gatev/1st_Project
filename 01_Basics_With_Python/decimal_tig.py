# import decimal
from decimal import Decimal

# price = 3 * 1.2
# print(price)
#
# price = Decimal("3 + 1.2")
print(3 * 1.2)
# a = Decimal('3')
a = 3
b = Decimal('1.2')
price = a * b
print(price)

a = 0.1
b = 0.1
c = 0.1
result = a + b + c
print(result)

a = Decimal(0.1)
b = Decimal(0.1)
c = Decimal(0.1)
result = a + b + c
print(result)

a = Decimal('0.1')
b = Decimal('0.1')
c = Decimal("0.1")
result = a + b + c
print(result)

a = 1.2
result = 3 * Decimal('NaN')
print(result)
