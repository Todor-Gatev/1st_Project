import re

# pattern = r"\b(?P<Day>\d{2})(?P<sep>[\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
pattern = r"\b(?P<Day>\d{2})([./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
# text1 = input()
text1 = "13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016"

num1 = re.findall(pattern, text1)
print(num1)
# print(*num1, sep=', ')
for num in num1:
    print(f"Day: {num[0]}, Month: {num[2]}, Year: {num[3]}")

# nums = re.finditer(pattern, text1)
# # print(nums)
# for num in nums:
#     num_dict = num.groupdict()
#     print(f"Day: {num_dict['Day']}, "
#           f"Month: {num_dict['Month']}, "
#           f"Year: {num_dict['Year']}")
#     print(f"Day: {num[1]}, "
#           f"Month: {num[3]}, "
#           f"Year: {num['Year']}")
#     print(num.group(0))
    # print(num.group(3))
    # print(num.group(4))
    # print(num)
    # print(type(num))
    # print(num_dict)
    # print(list(el) for el in num_dict)
