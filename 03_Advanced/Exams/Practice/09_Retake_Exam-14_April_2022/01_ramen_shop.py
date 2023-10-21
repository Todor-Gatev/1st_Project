from collections import deque

bowls = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    b = bowls.pop()
    c = customers.popleft()

    if b < c:
        c -= b
        customers.appendleft(c)
    elif b > c:
        b -= c
        bowls.append(b)

if not customers:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")


if bowls:
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
