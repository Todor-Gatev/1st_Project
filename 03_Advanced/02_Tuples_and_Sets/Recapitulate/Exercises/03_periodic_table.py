elements = set()

for _ in range(int(input())):
    elements.update(input().split())

print(*elements, sep="\n")
