data = input()

open_braces = []

for ch in data:
    if ch in "([{":
        open_braces.append(ch)
    else:
        if open_braces:
            if open_braces.pop() + ch in "[]{}()":
                continue

        print("NO")
        exit()

if open_braces:
    print("NO")
else:
    print("YES")
