from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(map(int, input().split(", ")))
i = 0

while i < 5 and chocolates and cups_of_milk:
    if chocolates[- 1] <= 0 or cups_of_milk[0] <= 0:
        chocolates.pop() if chocolates[- 1] <= 0 else None
        cups_of_milk.popleft() if cups_of_milk[0] <= 0 else None
        continue

    chocolate = chocolates.pop()
    cup = cups_of_milk.popleft()

    if chocolate != cup:
        cups_of_milk.append(cup)
        chocolates.append(chocolate - 5)
    else:
        i += 1

if i == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
