def sorting_cheeses(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for cheese, values in sorted_list:
        result += cheese + "\n" + "\n".join([str(x) for x in sorted(values, reverse=True)]) + "\n"

    return result[:-1]


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
