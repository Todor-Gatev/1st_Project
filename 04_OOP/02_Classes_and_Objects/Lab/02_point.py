class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


a = Point(3, 7)
print(a.__dict__)
print(Point.__dict__)

p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
