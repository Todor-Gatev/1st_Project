odd_set = set()
even_set = set()

for idx in range(1, int(input()) + 1):
    result = 0
    for ch in input():
        result += ord(ch)

    result /= idx
    result = int(result)

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

if sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=', ')
elif sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=', ')
else:
    print(*odd_set.difference(even_set), sep=', ')
