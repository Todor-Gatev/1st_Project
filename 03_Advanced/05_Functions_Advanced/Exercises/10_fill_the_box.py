def fill_the_box(*args):
    box_volume = args[0] * args[1] * args[2]
    idx = 3
    cubes_left = 0

    while args[idx] != "Finish":
        if box_volume <= 0:
            cubes_left += args[idx]
        else:
            box_volume -= args[idx]

            if box_volume < 0:
                cubes_left -= box_volume

        idx += 1

    if box_volume < 0:
        return f"No more free space! You have {cubes_left} more cubes."
    else:
        return f"There is free space in the box. You could put {box_volume} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
