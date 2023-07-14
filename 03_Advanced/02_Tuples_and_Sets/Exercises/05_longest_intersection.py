def get_set(set_data):
    set_start, set_end = map(int, set_data.split(','))
    return {x for x in range(set_start, set_end + 1)}


longest_intersection = []

for _ in range(int(input())):
    set1_data, set2_data = input().split('-')
    set1 = get_set(set1_data)
    set2 = get_set(set2_data)
    set1.intersection_update(set2)
    if len(set1) > len(longest_intersection):
        longest_intersection = list(set1)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
