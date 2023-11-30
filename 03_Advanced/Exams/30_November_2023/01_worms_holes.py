from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

num_of_worms_at_start = len(worms)
matchesCount = 0

while worms and holes:
    worm = worms.pop()

    if worm <= 0:
        continue

    hole = holes.popleft()

    if not worm == hole:
        worm -= 3
        worms.append(worm)

        continue

    matchesCount += 1

print(f"Matches: {matchesCount}" if matchesCount else "There are no matches.")

if worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")
elif matchesCount == num_of_worms_at_start:
    print("Every worm found a suitable hole!")
else:
    print("Worms left: none")

print(f"Holes left: {', '.join(str(x) for x in holes)}" if holes else "Holes left: none")
