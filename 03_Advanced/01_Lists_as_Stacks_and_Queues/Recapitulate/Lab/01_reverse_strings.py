from collections import deque

kid_names = deque(input().split())
n = int(input())

while len(kid_names) > 1:
    kid_names.rotate(-n + 1)
    print(f"Removed {kid_names.popleft()}")

print(f"Last is {kid_names[0]}")
