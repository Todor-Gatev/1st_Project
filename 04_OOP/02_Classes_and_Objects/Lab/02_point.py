class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


a = Point(3, 7)
print(a.__dict__)
