# region get_letters.__name__
# from functools import wraps
#
#
# def vowel_filter(function):
#     vowels = "aeiouy"
#
#     @wraps(function)
#     def wrapper():
#         return [x for x in function() if x in vowels]
#
#     return wrapper
#
#
# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
# print(get_letters.__name__)  # wrapper if not @wraps(function) else get_letters
# endregion


# region if not decorator @uppercase
def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper  # if wrapper() print(decorate). if wrapper print(decorate())


# @uppercase
def say_hi():
    return 'hello there'


decorate = uppercase(say_hi)  # if not decorator @uppercase
  # HELLO THERE

# print(say_hi)  # <function uppercase.<locals>.wrapper at 0x0000015FFA129EE0>
# print(say_hi())  # HELLO THERE

# endregion
