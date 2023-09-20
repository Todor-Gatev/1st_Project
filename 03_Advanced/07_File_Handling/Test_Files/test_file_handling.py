file_error_handling = open('recapitulate_error_handling.py')

# print(file_error_handling.read())
# print(file_error_handling.read(7))
# print(file_error_handling.read(7))
# print(file_error_handling.read(7))
#
#
# print(file_error_handling.readline())  # read just one line (1)
# print(file_error_handling.readline(3))  # read just one line (2) first 3 symbols
# print(file_error_handling.readline(7))  # read just one line (2) first 7 symbols
# print(file_error_handling.readline(7))  # read just one line (2) if no more symbols nothing is printed

# for line in file_error_handling:
#     print(line, end="")
#     # print(line)  # will add additional empty line after each line in file

file = open('python.txt', 'w')  # Creates or open the file
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file")
file.close()

file = open('python.txt', 'w')  # Creates or open the file.
# If the file exists, its overwritten
file.close()

# file = open('python.txt', 'a')  # Creates or open the file
# file.write("\nFile is reopened. New lines are added.\n")
# file.write("If we use 'a' mode")
# file.close()
