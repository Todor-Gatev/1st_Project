longest_intersection = []

for _ in range(int(input())):
    set1_data, set2_data = [list(map(int, el.split(','))) for el in input().split('-')]
    set1 = set(range(set1_data[0], set1_data[1] + 1))
    set2 = range(set2_data[0], set2_data[1] + 1)  # not necessary to be set
    set1.intersection_update(set2)  # not necessary set2 to be set

    if len(set1) > len(longest_intersection):
        longest_intersection = list(set1)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
