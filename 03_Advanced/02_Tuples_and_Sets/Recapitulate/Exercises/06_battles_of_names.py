odd_set = set()
even_set = set()

for i in range(int(input())):
    num = int(sum([ord(ch) for ch in input()]) / (i + 1))

    even_set.add(num) if num % 2 == 0 else odd_set.add(num)

odd_set_sum = sum(odd_set)
even_set_sum = sum(odd_set)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*even_set.symmetric_difference(odd_set), sep=", ")


