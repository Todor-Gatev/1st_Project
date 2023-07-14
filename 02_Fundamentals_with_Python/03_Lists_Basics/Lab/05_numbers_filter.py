n = int(input())

odd_string = []
even_string = []
positives_string = []
negatives_string = []

for _ in range(n):
    num = int(input())

    if num < 0:
        negatives_string.append(num)
    else:
        positives_string.append(num)

    if num % 2 == 0:
        even_string.append(num)
    else:
        odd_string.append(num)

str_type = input()

if str_type == "even":
    print(even_string)
elif str_type == "odd":
    print(odd_string)
elif str_type == "negative":
    print(negatives_string)
else:
    print(positives_string)
