def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0],))

    return "\n".join(f"{name}: {qty}" for name, qty in kwargs)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
