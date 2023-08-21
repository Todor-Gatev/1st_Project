my_list = ['a', 'b', 'c', 'd']
a = ' - '.join(x for x in my_list)
print(a)
b = '\n'.join([f"- {x}" for x in my_list])
[print(f" - {x}") for x in my_list]
print(b)
