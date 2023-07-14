
price = 3 * 1.2
print(type(price))
print(price)
print(f"{price:.2f}")
# print(price:.2f)  # error

minutes = 5
seconds = 7
str_sec = "0" + str(seconds)
str_interpolation = f"{seconds:02d}"
# seconds is integer variable
print(f"{minutes}:{str_sec}")   #  5:07
print(f"{minutes}:0{seconds}")  #  5:07
print(str_interpolation)        #  07
print(f"{minutes}:{seconds:02d}")  #  5:07
