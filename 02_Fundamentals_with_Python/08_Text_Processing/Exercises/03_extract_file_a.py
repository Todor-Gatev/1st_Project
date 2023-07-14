path = input().split('\\')

file_and_ext = path[-1].split('.')
extension = file_and_ext.pop()

print(f"File name: {'.'.join(file_and_ext)}")
print(f"File extension: {extension}")
