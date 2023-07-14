# for i in range(1, 11):
#     print(i)                    # 1,2,3,4,5,6,7,8,9,10
# for i in range(10):
#     print(i)                    # 0,1,2,3,4,5,6,7,8,9
# for _ in range(3):
#     print("Hi")                   # Hi, Hi, Hi
# for i in range(8, 11):
#     print(i)                    # 8, 9, 10
# for i in range(-8, 3):
#     print(i)
# for i in range(11, 0, -2):
#     print(i, end=" ")           # 11 9 7 5 3 1

# print(sum(range(5)))   # 10
#
# for i in range(5):
#     print(i)           # 0, 1, 2, 3, 4
#
# print(list(range(5)))  # [0, 1, 2, 3, 4]

# text = "SoftUni"     # len - Return the number of items in a container.
# print(len(text))     # 7
# text = "Soft"
# print(len(text))     # 4
# text = "123456789"
# print(len(text))     # 9

# text = "So23un7"
# letter = text[1-1]     # S
# ## letter = text[3]     # 3
# ## letter = text[4]     # u
# print(text[1])       # o
# print(letter)        # S
# print(text[7-1])       # o
#
# for i in "So23un7":
#     print(i)
# else:
#     print("SoftUni")

# for _ in range(3):
#     name = input("Enter valid name: ")
#     if name == "End":
#         print("End of loop! No final else")
#         break
#     else:
#         print(f"Hello {name}!\n")
# else:
#     print("Loop finished.")

for i in range(1, 101):
    if i % 2 != 0:
        continue
    elif i == 14:
        break
    print(i, end=", ")    # 2, 4, 6, 8, 10, 12,
