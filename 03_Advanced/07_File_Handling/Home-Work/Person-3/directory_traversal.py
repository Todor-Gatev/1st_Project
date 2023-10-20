import os

files = {}
directory = "."
# directory = os.path.dirname(os.path.abspath(__file__))


def get_files(folder, level):
    if level == -1:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f, level - 1)
        # for el in os.listdir(f):
        #     filename = os.path.join(f, el)
        #     if os.path.isfile(filename):
        #         ext = el.split(".")[-1]
        #         if ext not in files:
        #             files[ext] = []
        #         files[ext].append(el)


get_files(directory, 1)
with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, filenames in sorted(files.items()):
        output_file.write(f"{ext}.\n")
        for filename in sorted(filenames):
            output_file.write(f"- - - {filename}\n")