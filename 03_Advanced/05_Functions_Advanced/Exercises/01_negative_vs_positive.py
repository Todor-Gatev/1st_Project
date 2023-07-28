def negative_vs_positive(*args):
    negative = 0
    positive = 0

    for num in args:
        num = int(num)
        if num < 0:
            negative += num
        else:
            positive += num

    print(negative)
    print(positive)

    if positive > -negative:
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


negative_vs_positive(*input().split())
