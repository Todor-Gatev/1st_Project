class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_ch_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(value)):
            if i != 0 and roman_ch_to_int[value[i]] > roman_ch_to_int[value[i - 1]]:
                result += roman_ch_to_int[value[i]] - 2 * roman_ch_to_int[value[i - 1]]
            else:
                result += roman_ch_to_int[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))

        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

