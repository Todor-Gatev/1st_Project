rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

n = 3
max_sum = -float("inf")
found_matrix = []

for i in range(rows - n + 1):
    for j in range(cols - n + 1):
        temp_matrix = [[matrix[i + y][j + x] for x in range(n)] for y in range(n)]
        current_sum = sum([num for list_t in temp_matrix for num in list_t])

        if current_sum > max_sum:
            max_sum = current_sum
            found_matrix = temp_matrix.copy()

print(f"Sum = {max_sum}")

[print(*list_i) for list_i in found_matrix]
