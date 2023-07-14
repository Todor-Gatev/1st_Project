def get_sum_of_even_and_odd_digits(number_as_str):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for el in number_as_str:
        if int(el) % 2 == 0:
            sum_of_even_digits += int(el)
        else:
            sum_of_odd_digits += int(el)

    result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

    return result


user_num_as_str = input()

print(get_sum_of_even_and_odd_digits(user_num_as_str))
