from collections import deque

monsters = deque(int(x) for x in input().split(','))
strikes = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters and strikes:
    m = monsters.popleft()
    s = strikes.pop()

    if m > s:
        monsters.append(m - s)
    else:
        killed_monsters += 1
        s -= m

        if s:
            if strikes:
                strikes[-1] += s
            else:
                strikes.append(s)

if not monsters:
    print("All monsters have been killed!")

if not strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")
