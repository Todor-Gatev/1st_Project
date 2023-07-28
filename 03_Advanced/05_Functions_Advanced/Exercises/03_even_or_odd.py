def even_odd(*args):
    action = args[-1]
    odd_res = []
    even_res = []

    for num in args[:-1]:
        num = int(num)

        if num % 2 == 0:
            even_res.append(num)
        else:
            odd_res.append(num)

    if action == "even":
        return even_res

    return odd_res


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
