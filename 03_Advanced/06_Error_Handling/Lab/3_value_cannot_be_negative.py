class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    a = int(input())

    if a < 0:
        raise ValueCannotBeNegative
