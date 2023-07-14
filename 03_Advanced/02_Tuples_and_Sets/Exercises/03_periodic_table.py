n_set = set()

for _ in range(int(input())):
    # n_set.update(set(input().split()))
    n_set.update(input().split())

print(*n_set, sep='\n')
