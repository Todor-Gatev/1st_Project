# region Class Decorator

class func_logger:
    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)
        # return f"{self.func(*args)} - tested"


@func_logger
def say_hi(name):
    print(f"Hi, {name}")


@func_logger
def say_bye(name):
    print(f"Bye, {name}")


say_hi("Peter")  # Hi, Peter + out.log file containing self.func.__name__ + " was called"
say_bye("Peter")  # Bye, Peter + out.log file containing self.func.__name__ + " was called"

# endregion


# region class Fibonacci

# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, n):
#         if n not in self.cache:
#             if n == 0:
#                 self.cache[0] = 0
#             elif n == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[n] = self(n - 1) + self(n - 2)
#                 # self.cache[n] = self(n - 1)
#                 # self.cache[n] = self(n + 1) + self(n - 2)  # infinite recursion
#                 # self.cache[n] = self(n - 1) + self(n + 2)  # infinite recursion
#         return self.cache[n]
#
#
# # with self.cache = {} we did not calculate the staff calculated yet
# fib = Fibonacci()
# print(fib(7))  # 7 can be entered because of n in def __call__(self, n):
# # print(fib(7))  # 7 can be entered because of n in def __call__(self, n):
# # print(fib(9))  # 9 can be entered because of n in def __call__(self, n):
#
# for i in range(7+1):  # with self.cache = {} we do not calculate the calculated staff again
#     print(fib(i))
#     print(fib.cache)
#
# print(fib.cache)  # {1: 1, 0: 0, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}

# endregion


# region @repeat(3)

# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(3)
# def say_hi():
#     print("Hello")
#
#
# say_hi()  # Hello\n Hello\n Hello\n
# print(say_hi())  # Hello\n Hello\n Hello\n + None - because say_hi() doesn't have return

# endregion

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

# def uppercase(function):
#     def wrapper():
#         result = function()
#         uppercase_result = result.upper()
#         return uppercase_result
#
#     return wrapper  # if wrapper() print(decorate). if wrapper print(decorate())
#
#
# # @uppercase
# def say_hi():    # with decorator @uppercase - say_hi() - becomes wrapper() - in def uppercase(function)
#     return 'hello there'
#
#
# decorate = uppercase(say_hi)  # if not decorator @uppercase
# print(decorate())  # HELLO THERE
#
# # print(say_hi)  # <function uppercase.<locals>.wrapper at 0x0000015FFA129EE0>
# # print(say_hi())  # HELLO THERE

# endregion
