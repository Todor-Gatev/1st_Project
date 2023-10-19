from collections import deque

milligrams = [int(x) for x in input().split(", ")]
drinks = deque(int(x) for x in input().split(", "))
caffeine = 0

while milligrams and drinks:
    m = milligrams.pop()
    d = drinks.popleft()
    r = m * d

    if r + caffeine <= 300:
        caffeine += r
    else:
        drinks.append(d)
        caffeine -= 30
        caffeine = max(caffeine, 0)

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine} mg caffeine.")
