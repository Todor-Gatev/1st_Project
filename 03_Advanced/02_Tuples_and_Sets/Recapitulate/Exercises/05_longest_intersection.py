length_longest_intersection = 0

result = []

for _ in range(int(input())):
    first, second = input().split("-")
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    set1 = set(range(first_start, first_end + 1))
    set2 = set(range(second_start, second_end + 1))

    if len(set1.intersection(set2)) > length_longest_intersection:
        length_longest_intersection = len(set1.intersection(set2))
        result = list(set1.intersection(set2))

print(f"Longest intersection is {result} with length {length_longest_intersection}")
