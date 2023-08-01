# a = {1, 2, 3, 5, 6}
# b = {1, 2, 3, 5, 4}
ages = [5, 12, 17, 18, 24, 32]
adults = list(filter(lambda x: x > 17, ages))
print(type(adults))
print(adults)

for z in adults:
    print(z)
    print(type(z))
