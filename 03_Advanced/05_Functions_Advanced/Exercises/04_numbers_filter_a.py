# look at the other solution!!!
def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "odd":
            kwargs[key] = list(filter(lambda x: x % 2 == 1, kwargs[key]))
        elif key == "even":
            kwargs[key] = list(filter(lambda x: x % 2 != 1, kwargs[key]))

    kwargs = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

    return kwargs


# look at the other solution!!!
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
