def sorting_cheeses(**kwargs):
    res = ""
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for cheese, values in sorted_cheese:
        values.sort(reverse=True)
        res += cheese + "\n" + "\n".join(str(x) for x in values) + "\n"

    return res[:-1]


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
