from collections import deque

chocolates = list(map(int, input().split(', ')))
cups = deque(map(int, input().split(', ')))
milkshakes = 0

while cups and chocolates:
    cup = cups.popleft()
    chocolate = chocolates.pop()

    if cup <= 0 and chocolate <= 0:
        continue
    elif chocolate <= 0:
        cups.appendleft(cup)
        continue
    elif cup <= 0:
        chocolates.append(chocolate)
        continue

    if cup == chocolate:
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        cups.append(cup)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end='')
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if cups:
    print("Milk: ", end='')
    print(*cups, sep=", ")
else:
    print("Milk: empty")

print(f"Milk: {', '.join(str(x) for x in cups) or 'empty'}")
