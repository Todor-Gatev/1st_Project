words = input().split()

result = [(word * len(word)) for word in words]
print(*result, sep='')

# result = ""
#
# for string in words:
#     length = len(string)
#     result += string * length
#     # for _ in range(len(string)):
#     #     print(string, end='')
#
# print(result)
