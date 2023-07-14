from math import floor
from math import sqrt


def is_line_one_longer(x1, y1, x2, y2):
    line_1_length = sqrt((x1 ** 2) + (y1 ** 2))
    line_2_length = sqrt((x2 ** 2) + (y2 ** 2))

    return line_1_length >= line_2_length
    # if dist_2_squared < dist_1_squared:
    #     first_line_is_longer = False
    #     return first_line_is_longer
    # else:
    #     first_line_is_longer = True
    #     return first_line_is_longer


x = [0]
y = [0]

for i in range(4):
    x.append(floor(float(input())))
    y.append(floor(float(input())))

x_1 = (x[1] - x[2])
y_1 = (y[1] - y[2])
x_2 = (x[3] - x[4])
y_2 = (y[3] - y[4])

if is_line_one_longer(x_1, y_1, x_2, y_2):
    print(f"({x[2]}, {y[2]})({x[1]}, {y[1]})")
    # if x[1] > x[2]:
    #     print(f"({x[1]}, {y[1]})({x[2]}, {y[2]})")
    # else:
    #     print(f"({x[2]}, {y[2]})({x[1]}, {y[1]})")
else:
    print(f"({x[4]}, {y[4]})({x[3]}, {y[3]})")
    # if x[3] > x[4]:
    #     print(f"({x[3]}, {y[3]})({x[4]}, {y[4]})")
    # else:
    #     print(f"({x[4]}, {y[4]})({x[3]}, {y[3]})")
