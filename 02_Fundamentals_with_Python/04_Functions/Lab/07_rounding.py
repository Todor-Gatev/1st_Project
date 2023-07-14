def round_nums(numbers):
    result = []
    for num in numbers:
        result.append(round(num))

    return result


input_nums = [float(x) for x in input().split()]

print(round_nums(input_nums))
