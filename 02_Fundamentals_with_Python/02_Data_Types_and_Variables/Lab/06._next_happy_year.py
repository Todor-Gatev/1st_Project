# Read user input
year = int(input()) + 1

# str_year = str(year)
# set_str_year = set(str_year)

# Logic
# while len(str_year) != len(set_str_year):
while len(str(year)) != len(set(str(year))):
    year += 1
    # str_year = str(year)
    # set_str_year = set(str_year)
else:
    print(year)
# End of Logic
