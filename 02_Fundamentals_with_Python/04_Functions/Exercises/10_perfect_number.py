def is_divisor(num, a):
    return num % a == 0


number = int(input())
sum_divisors = 0

for i in range(1, number):
    if is_divisor(number, i):
        sum_divisors += i

if sum_divisors == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
