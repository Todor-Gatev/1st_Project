# from collections import deque

ch_list = list(input())

open_parenthesis = []

map_functions = {
    '(': lambda x: open_parenthesis.append(x),
    '[': lambda x: open_parenthesis.append(x),
    '{': lambda x: open_parenthesis.append(x),
    ')': lambda x: open_parenthesis.pop() if open_parenthesis[-1] == '(' else exit(print("NO")),
    ']': lambda x: open_parenthesis.pop() if open_parenthesis[-1] == '[' else exit(print("NO")),
    '}': lambda x: open_parenthesis.pop() if open_parenthesis[-1] == '{' else exit(print("NO")),
}

for ch in ch_list:
    if not open_parenthesis and ch in "]})":
        exit(print("NO"))

    map_functions[ch](ch)

if open_parenthesis:
    print("NO")
else:
    print("YES")
