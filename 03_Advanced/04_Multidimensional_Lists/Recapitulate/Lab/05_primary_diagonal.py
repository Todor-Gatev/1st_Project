n = int(input())
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    row = [int(x) for x in input().split()]
    primary_diagonal_sum += row[i]
    secondary_diagonal_sum += row[n - i - 1]

print(secondary_diagonal_sum)
