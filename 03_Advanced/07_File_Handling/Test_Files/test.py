# file = open('python1.txt', 'a')  # Creates or open the file
# file.write("\nFile is reopened. New lines are added.\n")
# file.write("If we use 'a' mode")
# file.close()

with open("file.txt", "w") as f:
    f.write("Hello World!!!")

