# Read user input
int_list = [int(x) for x in input().split(", ")]

groups = (max(int_list) + 9) // 10
low_boundary = 1
high_boundary = 10

# Logic
for i in range(1, groups + 1):
    list_of_numbers = [x for x in int_list if low_boundary <= x <= high_boundary]
    print(f"Group of {i * 10}'s: {list_of_numbers}")
    low_boundary += 10
    high_boundary += 10
# End of Logic
