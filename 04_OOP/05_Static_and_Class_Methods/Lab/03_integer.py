class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))

        return "value is not a float"

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"

    @classmethod
    def from_roman(cls, value):
        ch_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(value)):
            if i != 0 and ch_num[value[i]] > ch_num[value[i - 1]]:
                res += ch_num[value[i]] - 2 * ch_num[value[i - 1]]
            else:
                res += ch_num[value[i]]

        return cls(res)


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

tr = Integer.from_float(2.6)
print(tr.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
