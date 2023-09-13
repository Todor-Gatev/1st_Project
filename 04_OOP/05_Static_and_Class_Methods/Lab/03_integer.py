from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        try:
            cls(floor(float_value))
            return floor(float_value)
        except TypeError:
            return "value is not a float"

    @classmethod
    def from_string(cls, value):
        try:
            cls(int(value))
            return int(value)
        except ValueError:
            return "wrong type"


# first_num = Integer(10)
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))

# print(Integer.from_float("2.6"))
# print(Integer.from_float(2))

print(Integer.from_string("2.6"))
print(Integer.from_string(2.6))
