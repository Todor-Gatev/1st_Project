def shopping_cart(*args):
    if args[0] == "Stop":
        return "No products in the cart!"

    meals = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }

    for info in args:
        if info == "Stop":
            break

        if info[0] == "Soup" and len(meals["Soup"]) < 3:
            meals["Soup"].add(info[1])
        elif info[0] == "Pizza" and len(meals["Pizza"]) < 4:
            meals["Pizza"].add(info[1])
        elif info[0] == "Dessert" and len(meals["Dessert"]) < 2:
            meals["Dessert"].add(info[1])

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0],))
    result = []

    for meal, products in sorted_meals:
        p = list(sorted(products))
        result.append(f"{meal}:")
        result.extend(f" - {x}" for x in p)

    return "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
