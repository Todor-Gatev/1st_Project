# print('Hello, ', end='')
# print('Hello, ')
# print('Hello, \n' + 'Thanks')
# print('Hello, ', end='')

x = 4.5
y = 5.5
print(x,    'bravo', y)
print(f"{x} bravo {y}")         # 4.5 bravo 5.5
print(f"{x}_bravo_{y}")         # 4.5_bravo_5.5
print(f"{x}'bravo'{y}")         # 4.5'bravo'5.5
print(f"{x} + 'bravo' + {y}")   # 4.5 + 'bravo' + 5.5

# string_text = str(str(x), "bravo", y)
# string_text = str(x), 'bravo', str(y)
string_text = f"{x} bravo {y}"
# string_text = str(x) + 'bravo' + str(y)
# string_text = str(x)
print(string_text)          # (4.5, 'bravo', 5.5)
print(type(string_text))    # <class 'tuple'>
# print(x + 'bravo' + y)    # Error -> Expected type 'float', got 'str' instead


for year in range(1, 5):     # will iterate 4 times again
    year -= 1                # will iterate 4 times again
    print(year, end=' ')     # 0 1 2 3
