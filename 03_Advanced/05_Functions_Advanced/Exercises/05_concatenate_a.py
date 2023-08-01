# look at the other solution!!!
def concatenate(*args, **kwargs):
    res = "".join(args)

    for key in kwargs:
        if key in res:
            res = res.replace(key, kwargs[key])

    return res


# look at the other solution!!!
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
