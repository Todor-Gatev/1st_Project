# from math import *
# x = 5.98
# print(math.floor(x))   #-> not floor(x)
# print(math.ceil(x))    #-> not ceil(x)
# print(int(x))          #=> floor(x)
#
# from math import *
# x = 5.98
# print(floor(x))   #-> not floor(x)
# print(ceil(x))    #-> not ceil(x)
# print(int(x))          #=> floor(x)


# x = 4.5
# print(f'{x:.0f}')
# y = 5.5
# print(f'{y:.0f}')
# print(x, 'bravo', y)

# print(sum(range(2, 5)))
# for i in range(-2, 3):
#     print(i)

# for i in range(97, 102):
#     print(chr(i))
#
# for char in "abc":
#     print(ord(char))
#
# for char in "abc":
#     print(char)


# for i in range(0, 5, int(1.5)):
#     print(i, end='   ')
#
# counter = 3
#
# while counter <= 7:
#     print(counter)
#     counter += 1

# name = input()

# while name != 'stop':
#     print(f'Your name is: {name}')
#     name = input()

# while True:
#     name = input()
#     if name == 'stop':
#         print('End of loop')
#         break
#     print(f'Your name is: {name}')

# counter = 0

# while True:
#     counter += 1
#     print('s')
#
#     if counter == 4:
#         break


# counter = 0
# while counter < 5:
#     counter += 1
#     if counter == 3:
#         continue
#     print(counter)      # 1 2  4 5

# text = "So23un"
# letter = text[0] + text[1]     # S
# letter = text[1-1]   # S
# letter = text[3]     # 3
# letter = text[4]     # u
# print(text[2])       # o
# print(letter)

x = 7
print(f'{x:5d}')

number = int(input())
is_valid = 100 <= number <= 200 or number == 0
if not is_valid:
    print('invalid')

x = 2.45
y = 5
w = x // 2
print(type(w))
w = y // 2
print(type(w))
