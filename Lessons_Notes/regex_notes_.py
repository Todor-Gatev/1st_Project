import re

# ([0]|[1-9][0-9]*) -> matches 0 but not 00 or 01
# (?:   ) - does not capture/assign a group ID.
# (   ) - group with ID. \+359([\s-])\d\1 -> \1 recall group with ID=1 ([\s-])
# (?P<name>   ) - group with name. \+359(?P<sep>[\s-])\d(?P=sep) -> (?P=sep) recall group (?P<sep>[\s-])
# \b - only letters, nums and _, but not +-@....
# ([0]|[1-9]\d*)(\.\d+)? vs ([0]|[1-9]\d*\.?\d+)
# \w [a-zA-Z0-9_] be careful for _ !!!!!!
# (^|(?<=\s)) new line or space
# (^|\s) new line or space, but add the space to the result

# word = input()
# pattern = rf'\b{word}\b'  #  rf''

# word = input().casefold()
# pattern = rf'\b{word}\b'  # -> how?
# # matches = re.findall(rf'(^|(?<=\s)){word}($|(?=\s))', text) # will not much HOW+?
# matches = re.findall(rf'\b{word}\b', text)
# print(len(matches))

# if there is more than 1 group, do not use re.findall(), but re.finditer or (?:...)
# (?:...) means do not create a group ID, but act as a group

# result = re.findall() # finds all, returns list
# result = re.search() # finds first, not iterable, returns match type or None
# re.match is anchored at the start
# re.fullmatch is anchored at the start and end of the pattern
# re.search is not anchored
# result = re.match() # finds first, if it's at the beginning only, but
# if re.search(pattern, names):
#     print("yes")
# else:
#     print("no")


# pattern = r"\b(?P<Day>\d{2})([./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"
pattern = r"\b(?P<Day>\d{2})(?P<sep>[\./-])(?P<Month>[A-Z][a-z][a-z])(?P=sep)(?P<Year>\d{4})\b"
text1 = "13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016"
dates = re.finditer(pattern, text1)
# print(dates)
for date in dates:
    print(date)
    num_dict = date.groupdict()  # Match into dict
#     print(f"Day: {num_dict['Day']}, "  # calling value of key=Day from num_dict
#           f"Month: {num_dict['Month']}, "
#           f"Year: {num_dict['Year']}")
#     print(f"Day: {num[1]}, "  # group(1) returns the group(1) Match
#           f"Month: {num[3]}, "  # group(3) returns the group(3) Match
# #         f"Month: {num['Month']}" <=> f"Month: {num[3]}" -> both can be used
#           f"Year: {num['Year']}")  # group(Year)(4) returns the group(Year)(4) Match
# #         f"Year: {num['Year']}" <=> f"Year: {num[4]}"
# #         -> both num['Year'] and num[4] can be used, because group4 is named Year
    print(f"Day: {num_dict['Day']}, Month: {num_dict['Month']}, Year: {num_dict['Year']}")
    print(f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}")
    print(f"Day: {date[1]}, Month: {date.group(3)}, Year: {date[4]}")
    # !!! use date.group(1) or date.group('Day'), but not date[1] or date['Day'],
    # because it could NOT be available in next release!!!
    print(date.group())  # group(0) returns the whole Match
    print(date.group(1))  # group(1) returns Day
    print(date.group('Month'))  # group(2) returns 'Month'
    print(date.groups())  # all groups as tuple ('13', '/', 'Jul', '1928')
# dates1 = re.findall(pattern, text1)
# print(dates1)
# for date in dates1:
#     print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
dates = re.match(pattern, text1)  # MATCH IS NOT ITERABLE, searches at the BEGINNING ONLY
print(dates)  # match & search are same type, but the scope
print(type(dates))
print(dates.groupdict())
dates = re.search(pattern, text1)  # returns the same as match, BUT in ALL ROWS
print(dates)  # match & search are same type, but the scope
print(type(dates))
print(dates.groupdict())

# txt = "The rain in Spain"
# x = re.sub(r"\s", "9", txt, 2)  # substitute(replace)
# print(x)
#
# txt = "The rain in Spain"
# x = re.split(r"\s", txt)
# print(x)

# text1 = input()
# text2 = input()
# text3 = input()
# pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
# num1 = re.findall(pattern, text1)  # more time
# num2 = re.findall(pattern, text2)  # more time
# num3 = re.findall(pattern, text2)  # more time
# regex_pattern = re.compile(pattern)
# num11 = regex_pattern.findall(text1)  # faster
# num12 = regex_pattern.findall(text2)  # faster
# num13 = regex_pattern.findall(text3)  # faster

# print(*res_list, sep=', ')
# print(str_res[:-2])
