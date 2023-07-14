from math import floor


def get_closest_to_center(x1, y1, x2, y2):
    dist_1_squared = (x1 ** 2) + (y1 ** 2)
    dist_2_squared = (x2 ** 2) + (y2 ** 2)

    if dist_2_squared < dist_1_squared:
        return f"({floor(x2)}, {floor(y2)})"
    else:
        return f"({floor(x1)}, {floor(y1)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(get_closest_to_center(x_1, y_1, x_2, y_2))
