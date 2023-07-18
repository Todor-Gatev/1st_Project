n, m = [int(x) for x in input().split(", ")]

matrix_2d = []
total_sum = 0

for i in range(n):
    a = list(map(int, input().split(", ")))
    total_sum += sum(a)
    matrix_2d.append(a)

print(total_sum)
print(matrix_2d)
