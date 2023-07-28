def sort_descending(x):
    return -len(x[1])


def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [x for x in kwargs["odd"] if x % 2 != 0]

    if "even" in kwargs:
        kwargs["even"] = [x for x in kwargs["even"] if x % 2 == 0]

    if "odd" not in kwargs or "even" not in kwargs:
        return kwargs

    # kwargs = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
    kwargs = dict(sorted(kwargs.items(), key=sort_descending))

    return kwargs


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
