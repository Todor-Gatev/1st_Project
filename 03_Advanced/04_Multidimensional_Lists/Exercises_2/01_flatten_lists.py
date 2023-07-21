matrix = [x.split() for x in input().split("|")]

print(*[el for list_i in matrix[::-1] for el in list_i])
