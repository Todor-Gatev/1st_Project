# file = open('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/zzz_text.py')
# file = open('W:\1_Python\1-Training\1_Projects\1st_Project\Lessons_Notes\zzz_text.py')  # wrong

# print(file.read())


# region File Open
# region FileNotFoundError if not on sofa PC
# try:
#     file = open('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/File_Handling_Notes/text.txt', 'r')
#     # FileNotFoundError if not on sofa PC
#     file.close()
# except FileNotFoundError:
#     print("File not found or path is incorrect")
# finally:
#     print("exit")
# endregion


# region no errors
# try:
#     file = open('text.txt', 'r')
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("File not found or path is incorrect")
# finally:
#     print("exit")
# endregion
# endregion


# To avoid unwanted behaviour always close the files
# Files opened with "with" statement will be closed automatically once it leaves the "with" block
with open("file.txt", "w") as f:
    f.write("Hello World!!!")
    print(f.read())  # Error: io.UnsupportedOperation: not readable if the file is open for writing or adding 'a'

# region Create and Edit Files
# w - open for writing, truncating the file first
# file = open('python.txt', 'w')  # Creates or open the existing file(make it empty blank first)
# file.write("This is the write command.\n")
# file.write("It allows us to write in a particular file")
# file.close()

# file = open('python.txt', 'a')  # Creates or open the file.
# file.write("\nFile is reopened. New lines are added.\n")
# file.write("If we use 'a' mode")
# # print(file.read())  # io.UnsupportedOperation: not readable
# file.close()

# file = open('text.txt')  # => open('python.txt', 'r')
# # print(file.read())
# # print(file.read(7))  # will print nothing if file has been read already
# # print(file.readline())
# # print(file.readline(7))
# for line in file:
#     # print(line)  # will add additional empty line after printing each line of file
#     print(line, end="")  # will print nothing if file has been read already
#     print(line.split())
#
# print(file.read())  # will print nothing if file  has been read in "for line in file" already
# file.close()

# lines = ["Write ", "in ", "file"]
# with open('python1.txt', 'a') as pyt, open('file.txt') as f:  # opens multiple files
#     pyt.writelines(lines)  # Write multiple strings
#     pyt.write("\n")
#     print(f.read())

# endregion


# region Delete File
# import os

# file_path = "text.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)

# try:
#     os.remove('text.txt')
# except FileNotFoundError:
#     print('File already deleted!')

# recreate the file again for the next test
# with open("text.txt", "w") as f:
#     f.write("Hello World!!!")

# endregion


# region Directory manipulation
# import os
#
#
# # print(os.mkdir('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/File_Handling_Notes/Test_Folder'))
# print(os.getcwd())  # Return a string representing the current working directory.
# # os.mkdir('Test')
# # os.rmdir('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/File_Handling_Notes/Test_Folder')
# # os.chdir('Test_Folder')
# print(os.listdir('W:/1_Python/1-Training/1_Projects/1st_Project'))

# os.path.isfile(path) # method that returns True if the path is a file or a symlink to a file.
# os.path.exists(path) # method that returns True if the path is a file, directory, or a symlink to a file.

# endregion
