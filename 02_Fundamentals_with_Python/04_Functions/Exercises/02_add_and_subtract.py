def add(a, b):
    result = a + b
    return result


def subtract(a, b, c):
    result = add(a, b) - c
    return result


x = int(input())
y = int(input())
z = int(input())

# print(subtract(add(x, y), z))
print(subtract(x, y, z))
