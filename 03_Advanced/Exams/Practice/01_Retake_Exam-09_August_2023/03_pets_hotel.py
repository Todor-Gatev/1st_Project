def accommodate_new_pets(capacity: int, max_weight: float, *args):
    accommodated_pets = {}
    result = ""

    for pet in args:
        if not capacity:
            result = "You did not manage to accommodate all pets!\n"
            break

        if pet[1] <= max_weight:
            capacity -= 1
            accommodated_pets[pet[0]] = accommodated_pets.get(pet[0], 0) + 1
    else:
        result = f"All pets are accommodated! Available capacity: {capacity}.\n"

    accommodated_pets = sorted(accommodated_pets.items(), key=lambda x: x[0])
    result += "Accommodated pets:\n" + "\n".join(f"{pet_type}: {qty}" for pet_type, qty in accommodated_pets)

    return result


# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))

# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
