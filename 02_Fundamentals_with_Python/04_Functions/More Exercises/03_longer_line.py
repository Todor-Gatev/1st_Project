from math import floor
from math import sqrt


def is_line_one_longer(x1, y1, x2, y2):
    line_1_length = sqrt((x1 ** 2) + (y1 ** 2))
    line_2_length = sqrt((x2 ** 2) + (y2 ** 2))

    return line_1_length >= line_2_length


def get_closest_to_center(x1, y1, x2, y2):
    dist_1_squared = (x1 ** 2) + (y1 ** 2)
    dist_2_squared = (x2 ** 2) + (y2 ** 2)

    if dist_2_squared < dist_1_squared:
        return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"


x = [0]
y = [0]

for i in range(4):
    x.append(float(input()))
    y.append(float(input()))

x_1 = (x[1] - x[2])
y_1 = (y[1] - y[2])
x_2 = (x[3] - x[4])
y_2 = (y[3] - y[4])

if is_line_one_longer(x_1, y_1, x_2, y_2):
    print(get_closest_to_center(x[1], y[1], x[2], y[2]))
else:
    print(get_closest_to_center(x[3], y[3], x[4], y[4]))
