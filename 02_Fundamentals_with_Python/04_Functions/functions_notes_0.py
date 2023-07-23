# def add_number_12(list_seq):
#     list_seq.append(12)
# # no return but amends
#
#
# nums = [1, 2, 3]
# print(nums)  # [1, 2, 3]
# add_number_12(nums)  # no return but amends nums because list are reference
# print(nums)  # [1, 2, 3, 12]

# def add_number_12(set_seq):
#     set_seq.add(12)
# # no return but amends
#
#
# set_nums = {1, 2, 3}
# print(set_nums)  # {1, 2, 3}
# add_number_12(set_nums)  # no return but amends nums because set are reference
# print(set_nums)  # {1, 2, 3, 12}

def add_key_test(dict_seq):
    dict_seq.update({"test": 7})
# no return but amends


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car)  # {{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
add_key_test(car)  # no return but amends car because dict are reference
print(car)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'test': 7}


# def give_me_another_five(a):
#     a = 5
#
#
# num = 7
# print(num)  # 7
# print(give_me_another_five(num))  # None
# print(num)  # 7 not amended, because float, str, int are not a reference


# def give_me_another_five(a):
#     a = 9.3
#
#
# a = 5.7
# print(a)  # 5.7
# print(give_me_another_five(a))  # None
# print(a)  # 5.7 not amended, because float, str, int are not a reference
