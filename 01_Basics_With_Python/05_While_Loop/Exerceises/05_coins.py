# from math import ceil

# Read user input
change = float(input())

# Logic
coins = round(change * 100)
coins_counter = 0

temp_count = coins // 200
coins_counter += temp_count
coins %= 200
temp_count = coins // 100
coins_counter += temp_count
coins %= 100
temp_count = coins // 50
coins_counter += temp_count
coins %= 50
temp_count = coins // 20
coins_counter += temp_count
coins %= 20
temp_count = coins // 10
coins_counter += temp_count
coins %= 10
temp_count = coins // 5
coins_counter += temp_count
coins %= 5
temp_count = coins // 2
coins_counter += temp_count
coins %= 2
temp_count = coins // 1
coins_counter += temp_count


# Print Output
print(coins_counter)
# print(f'{coins_counter:.0f}')

# Logic
# coins_counter = 0
# leva = int(change)
# coins = round((change - leva) * 100)
# temp_count = 0
#
# if leva != 0:
#     two_leva_coins = leva // 2
#     one_leva_coins = leva % 2
#     coins_counter = one_leva_coins + two_leva_coins
#
# if coins != 0:
#     temp_count = coins // 50
#     coins_counter += temp_count
#     coins %= 50
#     temp_count = coins // 20
#     coins_counter += temp_count
#     coins %= 20
#     temp_count = coins // 10
#     coins_counter += temp_count
#     coins %= 10
#     temp_count = coins // 5
#     coins_counter += temp_count
#     coins %= 5
#     temp_count = coins // 2
#     coins_counter += temp_count
#     coins %= 2
#     temp_count = coins // 1
#     coins_counter += temp_count
#     coins %= 1
