ch_list = list(input())

open_parenthesis = []

for ch in ch_list:
    if ch in "({[":
        open_parenthesis.append(ch)
    elif not open_parenthesis:
        exit(print("NO"))
    else:
        if (open_parenthesis[-1] + ch) not in "(){}[]":
            exit(print("NO"))

        open_parenthesis.pop()

if open_parenthesis:
    print("NO")
else:
    print("YES")
