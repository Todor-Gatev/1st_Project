from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
paper_size = deque(int(x) for x in input().split(", "))

boxes = 0

while eggs_size and paper_size:
    if eggs_size[0] <= 0:
        eggs_size.popleft()
        continue
    elif eggs_size[0] == 13:
        eggs_size.popleft()
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0],
        continue

    e = eggs_size.popleft()
    p = paper_size.pop()

    if e + p <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")
