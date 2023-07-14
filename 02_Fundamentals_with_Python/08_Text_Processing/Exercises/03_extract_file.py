path = input().split('\\')

file_and_ext = path[-1].split('.')
print(f"File name: {file_and_ext[0]}")
print(f"File extension: {file_and_ext[1]}")
