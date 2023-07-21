n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input()

while command != "END":
    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    if not (row in range(n) and col in range(n) and action in ["Add", "Subtract"]):
        print("Invalid coordinates")
    elif action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

    command = input()

[print(*matrix[row]) for row in range(n)]
