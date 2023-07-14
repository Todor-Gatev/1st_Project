txt = "Hi to  the life"
x = txt.split()       # ['Hi', 'to', 'the', 'life']
y = txt.split(' ')    # ['Hi', 'to', '', 'the', 'life']
z = txt.split('  ')   # ['Hi to', 'the life']
print(x)
print(y)
print(z)
print(txt)

# txt = "a, b ,   c d"
# x = txt.split()
# z = txt.split(', ')
# print(x)
# print(z)
# print(txt)
