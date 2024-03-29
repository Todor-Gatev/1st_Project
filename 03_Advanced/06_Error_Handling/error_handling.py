# methods are faster than try except!!!

# try:
#     times = int(input())
#     idx = int(input())
#     my_list = [1, 2, 3, 4, 5, 'a']
#     # times = float(input())
#     print(my_list[idx] / times)
# except ValueError as ex:
#     print(ex)  # invalid literal for int() with base 10: 'sgd'
# except ZeroDivisionError as text:
#     print("blabla")
#     print(text)  # division by zero
# except IndexError as idx_error:
#     print(idx_error)
# except (IndexError, ValueError) as idx_error:
#     print(idx_error)


# try:
#     # print("try")
#     a = 7
#     b = int(input())  # if b = 0 print("End") would not be executed, but print("finally")
#     c = a / b
# except ValueError as text:
#     print("ValueError")  # ValueError
#     print(text)  # invalid literal for int() with base 10: 'dhhfd'
# else:
#     print("from else")  # Not very useful. will be executed if successful try.
# finally:
#     print("finally")  # will always be executed
#
# print("End")  # if b = 0, code could not reach that line, because of error. if b = 'str' will print End.
# # if b = 0 -> ZeroDivisionError. if b = 'str' ValueError.

# try:
#     times = int(input())
#     # times = float(input())
# except ValueError as ex:
#     print(ex)
# except KeyError:
#     print()
# except NameError:
#     print()


my_list = [1, 2, 3, 4, 5, 'a']
# try:
#     # result = next(filter(lambda x: x == 1, my_list))
#     result = next(filter(lambda x: x == 7, my_list))
# except StopIteration:
# print("Not in list")
#
# print("in my_list")
def my_test(my_list):
    try:
        result = next(filter(lambda x: x == 1, my_list))
        # result = list(filter(lambda x: x == 1, my_list))[0]
        # result = next(filter(lambda x: x == 7, my_list))
    except StopIteration:
        return print("Not in list")

    return print(f"{result}: in my_list")
my_test(my_list)


# # custom exceptions
# class SmallValueException(Exception):
#     pass
#
#
# class HighValueException(Exception):
#     pass
#
#
# amount = float(input())  # you cannot transfer negative money
#
# if amount < 1:
#     raise SmallValueException("Amount can not be less than 1lv.")
# elif amount > 1000:
#     raise HighValueException("Transaction limit max 1000")
# # custom exceptions
