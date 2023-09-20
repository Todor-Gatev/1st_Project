# file = open('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/zzz_text.py')
# file = open('W:\1_Python\1-Training\1_Projects\1st_Project\Lessons_Notes\zzz_text.py')

# print(file.read())


# region FileNotFoundError if not on sofa PC
try:
    file = open('W:/1_Python/1-Training/1_Projects/1st_Project/Lessons_Notes/zzz_text.py.py', 'r')  # FileNotFoundError
except FileNotFoundError:
    print("File not found or path is incorrect")
finally:
    print("exit")
# endregion


# region no errors
try:
    file = open('zzz_text.py', 'r')
    print(file.read())
except FileNotFoundError:
    print("File not found or path is incorrect")
finally:
    print("exit")
# endregion
