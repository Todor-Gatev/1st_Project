# Note:
# All string methods returns new values.
# They do not change the original string.

# seconds = 7
# print(f"{seconds:03d}")   # 007
# print(f"{seconds:3d}")    # ..7
# num = 2.5584
# print(f"{num:.2f}")    # 2.56

# txt = "Hello, welcome to my world."
# print(txt.find("q"))  # -1 or index if q in txt
# print(txt.index("q"))  # Error or index if q in txt

# [::] no beginning and end
# a = "2371"
# x = a[::-1]  # 1732
# y = a[::-2]  # 13
# z = a[::2]   # 27
# b = list(a)  # ['2', '3', '7', '1']
# a = "0123456789"
# x1 = a[1::2]   # 13579
# x2 = a[::2]   # 02468
# x3 = a[::3]   # 0369
# c = list(a)
# c.extend(b)
# d = a[1:7]
# a = [1, 2, 3, 4, 5, 6, 7]
# b = a[-5:-2]  # new not referent
# b = a[-3:-6:-2]  # [5, 3]
# b = a[:]  # new not referent
# b = a[::]  # new not referent
# txt = "Welcome To My World"
# x = txt[-5::]  # World
# x = txt[-5:]  # World
# x = txt[14:]  # World
# x = txt[slice(-5, len(txt), 1)]  # World
# x = txt[slice(-5, 19, 1)]  # World
# x = txt[-5::2]  # Wrd
# x = txt[-5:2]  # empty because 2 = -17
# x = txt[-17:9]  # lcome T
# x = txt
# print(x)

# x = txt.casefold()  # stronger than lower()
# x = txt.lower()
# x = txt.count('l', 3, 19)  # string.count(value, start, end)
# x = "welcome".find("com")  # 3 string.find(value, start, end)
# x = "bob".center(10, '@')  # @@@bob@@@@
# x = txt.encode()  # string.encode(encoding=encoding, errors=errors)
# x = txt.endswith("my world.", 5, 11)  # True or False
# print("H\te\tl\tl\to".expandtabs(3)) # H  e  l  l  o
# print("H\te\tl\tl\to".expandtabs(5)) # H    e    l    l    o
# x = "welcome".isascii()  # True
# x = "wow_83".isidentifier()  # True
# x = "lo!\nAre".isprintable()  # False

# print(isinstance(11, float))  # False
# print(isinstance(11.0, int))  # False
# print(isinstance(11, float) or isinstance(11, int))  # True
# print(isinstance(11.0, float) or isinstance(11.0, int))  # True
# str_1 = "teststring12"
# x = str_1.isalnum()  # True - "alnum" - alpha numeric
# y = str_1.isalpha()  # False
# z = str_1.isdigit() # False Exponents, like ², are also considered to be a digit
# a = '-1'.isdecimal()   # False 0-9
# b = '3/4'.isnumeric()  # False
# c = '¾'.isnumeric()    # True 0-9 like ² and ¾
# d = "0.7"
# print('0.7'.isnumeric())  # False
# print("0.7".isdigit())  # False
# print(isinstance("0.7", float))  # False
# print(isinstance(0.7, float))  # True
# print(d.isnumeric())  # False – AttributeError if d=0.7 instead “0.7”
# print(d.isdigit())  # False – AttributeError if d=0.7 instead “0.7”
# print(isinstance(d, float))  # False


x = "ac"
y = "dc"
a = 5
b = 3
z = "band %s - %s" % (x, y)  # band ac - dc
w = "band %d - %d" % (a, b)  # band 5 - 3
# w = "band {} - {}".format(x, a)   # band ac - 5

print('   aabb  '.strip())
print('aabb  ')
print('   aabb  ')

txt = "Welcome To My World"
# x = txt.replace('l', '')  # Wecome To My Word
x = txt.replace('z', '')    # Welcome To My World
print(x)
