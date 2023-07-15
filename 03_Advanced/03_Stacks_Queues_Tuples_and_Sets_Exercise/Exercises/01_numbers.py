set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
check_subset = True if set_1.issubset(set_2) or set_1.issuperset(set_2) else False

map_functions = {
    "Add First": lambda x: set_1.update(x),
    "Add Second": lambda x: set_2.update(x),
    "Remove First": lambda x: set_1.difference_update(x),
    "Remove Second": lambda x: set_2.difference_update(x),
    "Check Subset": lambda x: print(check_subset)
    # "Check Subset": lambda x: print(True) if set_1.issubset(set_2) or set_1.issuperset(set_2)
    # else print(False)
}

for _ in range(int(input())):
    command = input().split()
    action = command[0] + ' ' + command[1]
    nums = set(map(int, command[2:]))
    # if map_functions.get(action):
    #     map_functions[action](nums)
    # else:
    #     print("KeyError")
    try:
        map_functions[action](nums)
    except KeyError:
        pass
        # print("KeyError")

print(*sorted(set_1), sep=', ')
print(*sorted(set_2), sep=', ')
