def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheese = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese, values in sorted_cheese:
        result += cheese + "\n"
        values.sort(reverse=True)
        result += "\n".join(str(x) for x in values)
        result += "\n"

    return result[:-1]


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
