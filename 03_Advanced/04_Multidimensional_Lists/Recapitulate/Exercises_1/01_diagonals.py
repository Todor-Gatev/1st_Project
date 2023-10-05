n = int(input())

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    line = [int(x) for x in input().split(", ")]
    primary_diagonal.append(line[i])
    secondary_diagonal.append(line[n - 1 - i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
