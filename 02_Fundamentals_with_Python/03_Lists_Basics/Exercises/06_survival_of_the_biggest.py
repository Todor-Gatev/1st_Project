# Read user input
list_of_integer = [int(x) for x in input().split()]
n = int(input())

# Logic
for _ in range(n):
    min_num = min(list_of_integer)
    list_of_integer.remove(min_num)
# End of Logic

# Print Output
print(', '.join(str(x) for x in list_of_integer))
