def fill_the_box(*args):
    volume = args[0] * args[1] * args[2]
    cubes = 0
    i = 3

    while args[i] != "Finish":
        cubes += args[i]
        i += 1

    if cubes > volume:
        return f"No more free space! You have {cubes - volume} more cubes."

    return f"There is free space in the box. You could put {volume - cubes} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2))
