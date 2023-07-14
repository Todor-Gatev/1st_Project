# Read user input
# number = int(input())
#
# # Logic
# if number != 0 and (number < 100 or number > 200):
#     print("invalid")

number = int(input())
valid = 100 <= number <= 200 or number == 0
if not valid:
    print('invalid')
