rows, cols = [int(x) for x in input().split(", ")]

matrix = []
total_sum = 0

for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)
    total_sum += sum(line)

print(total_sum)

# matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input().split(", ")[0]))]
print(matrix)
