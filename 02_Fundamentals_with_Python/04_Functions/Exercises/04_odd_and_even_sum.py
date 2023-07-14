def get_sum_of_even_and_odd_digits(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    while number:
        num = number % 10

        if num % 2 == 0:
            sum_of_even_digits += num
        else:
            sum_of_odd_digits += num

        number //= 10

    result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

    return result


user_num = int(input())

print(get_sum_of_even_and_odd_digits(user_num))
