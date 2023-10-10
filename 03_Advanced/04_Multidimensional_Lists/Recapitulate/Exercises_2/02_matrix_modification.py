n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break
    elif info[0] not in range(n) or info[1] not in range(n):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[info[0]][info[1]] += info[2]
    elif command == "Subtract":
        matrix[info[0]][info[1]] -= info[2]

[print(*row) for row in matrix]
