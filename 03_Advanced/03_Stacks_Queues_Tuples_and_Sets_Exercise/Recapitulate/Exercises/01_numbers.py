set1 = set(input().split())
set2 = set(input().split())

map_func = {
    "Add First": lambda x: set1.update(x),
    "Add Second": lambda x: set2.update(x),
    "Remove First": lambda x: set1.difference_update(x),
    "Remove Second": lambda x: set2.difference_update(x),
    # "Check Subset": lambda x: print(set1.issubset(set2) or set2.issubset(set1))
    "Check Subset": lambda x: print("True") if set1.issubset(set2) or set2.issubset(set1) else print("False")
}

for _ in range(int(input())):
    action1, action2, *info = input().split()

    map_func[action1 + ' ' + action2](info)

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
