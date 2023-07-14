# Read user input
n = int(input())
word = input()

str_list = []

# Logic
for _ in range(n):
    tmp_str = input()
    str_list.append(tmp_str)

print(str_list)

for i in range(len(str_list) - 1, -1, -1):
    el = str_list[i]

    if word not in el:
        str_list.remove(el)

print(str_list)
# End of Logic
