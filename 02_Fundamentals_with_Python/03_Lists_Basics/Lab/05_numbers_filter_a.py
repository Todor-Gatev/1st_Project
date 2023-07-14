n = int(input())

odd_string = []
even_string = []
positives_string = []
negatives_string = []
all_str = []

for _ in range(n):
    num = int(input())
    all_str.append(num)

str_type = input()

if str_type == "even":
    for i in range(len(all_str)):
        if all_str[i] % 2 == 0:
            even_string.append(all_str[i])
    print(even_string)
elif str_type == "odd":
    for i in range(len(all_str)):
        if all_str[i] % 2 != 0:
            odd_string.append(all_str[i])
    print(odd_string)
elif str_type == "negative":
    for i in range(len(all_str)):
        if all_str[i] < 0:
            negatives_string.append(all_str[i])
    print(negatives_string)
else:
    for i in range(len(all_str)):
        if all_str[i] >= 0:
            positives_string.append(all_str[i])
    print(positives_string)
