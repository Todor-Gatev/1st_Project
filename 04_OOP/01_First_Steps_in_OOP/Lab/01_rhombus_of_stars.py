def print_stars(i):
    print(' ' * (n - i), end='')
    print(*(['*'] * i))


def triangle_up():
    for i in range(1, n + 1):
        print_stars(i)


def triangle_down():
    for i in range(n - 1, 0, -1):
        print_stars(i)


def rhombus():
    triangle_up()
    triangle_down()


n = int(input())

rhombus()


# n = int(input())
#
# for i in range(1, n + 1):
#     print(' ' * (n - i), end='')
#     print(*(['*'] * i))
#
# for i in range(n - 1, 0, -1):
#     print(' ' * (n - i), end='')
#     print(*(['*'] * i))
