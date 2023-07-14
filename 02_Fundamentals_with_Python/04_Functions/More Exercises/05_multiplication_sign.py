def is_positive_result(a, b, c):
    is_positive = True
    if a < 0:
        is_positive = not is_positive

    if b < 0:
        is_positive = not is_positive

    if c < 0:
        is_positive = not is_positive

    return is_positive


x = int(input())
y = int(input())
z = int(input())

if x == 0 or y == 0 or z == 0:
    print("zero")
else:
    if is_positive_result(x, y, z):
        print("positive")
    else:
        print("negative")
