# for i in range(1, 5):
#     print(i * '*')

# for i in range(1, 5):
#     print(i * '*', end='')
#
# for i in range(1, 4):
#     print('*' * i)

# n = 3
# n = 5
# print('*' * n, end='\n')
# print('*' * n, end='')
# print('*' * n, end='\n')
# print('*' * n)
# print('*' * 3, '\n')
# print(3 * '*')
# print('*' * n, end='\n')

n = 16
print('*' * n, end='\n')

i = (n // 2) - 1
j = 2

# while i != 1:
#     while j < (n - 2):
#         print(i * '*', end='')
#         print(j * ' ', end='')
#         print(i * '*')
#
#         i -= 1
#         j += 2

while j < (n - 2):
    print(i * '*', end='')
    print(j * ' ', end='')
    print(i * '*')

    i -= 1
    j += 2
