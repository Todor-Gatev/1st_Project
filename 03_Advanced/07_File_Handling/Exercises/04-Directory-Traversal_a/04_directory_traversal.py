import os

folder_path = input()
data = []

# TODO: Use recursion. Dido exercise Advanced January 2023

for obj in os.listdir(folder_path):
    path = os.path.join(folder_path, obj)
    if os.path.isfile(path):
        data.append(obj.split('.'))

data.sort(key=lambda x: (x[-1], x[0]))

with open('report.txt', 'w') as report:
    extension = None

    for el in data:
        if el[-1] != extension:
            extension = el[-1]
            report.write(f".{extension}\n")
            report.write(f"{'- ' * 3}{el[0]}.{el[-1]}\n")
        else:
            report.write(f"{'- ' * 3}{el[0]}.{el[-1]}\n")

