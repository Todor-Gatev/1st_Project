def even_parameters(function):
    def wrapper(*args, **kwargs):
        pass

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
