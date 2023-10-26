from collections import defaultdict
# from collections import OrderedDict
d_test = {'a': [1, 2, 3], 'b': [4, 5, 6]}
d_test['c'] = d_test.pop('a')  # {'b': [4, 5, 6], 'c': [1, 2, 3]}
print(d_test)
# student_info = defaultdict(list)
# # student_info = defaultdict(lambda: [0.0])
# for _ in range(int(input())):
#     name, grade = input().split()
#     # if name not in student_info: this check can be omitted with defaultdict
#     #     student_info[name] = []
#     student_info[name].append(float(grade))

# x = ('key1', 'key2', 'key3')
# y = 0, 1, 2
# this_dict = dict.fromkeys(x)
# # this_dict = dict.fromkeys(x, y)
# print(this_dict)
# this_dict = dict(zip(x, y))
# print(this_dict)
#
# txt = "Hello, welcome to my world."
# print(txt.find("q"))  # -1 or index if q in txt
# print(txt.index("q"))  # Error or index if q in txt
#
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# x = car.items()
# print(car)
# print(type(car))
# print(x)
# print(type(x))
# for key, value in car.items():
#     print(key, value)

# x = car.setdefault("model", "Bronco")  # return Mustang if key exists
# print(x)
# print(car)
# y = car.setdefault("mod", "Bronco")  # add it and return Bronco if key does not exist
# print(y)
# print(car)
#
# car.update({"model": "laguna"})  # change value if key exists
# print(car)
# car.update({"test": "New_mod"})  # add key, value if key does not exist
# print(car)
# car["li"] = 5  # act as update
# print(car)
# car["model"] = "lag"  # act as update
# print(car)

# bus = {
#     "br": "Fo",
#     "model": "Mus",
#     "ye": 19
# }
# # car.setdefault(bus)  # Error - requires (key, value)
# # car.update("model", "Bronco")  # Error - requires dict
# car.update(bus)  # requires dict {key, value}
# print(car)


# x = car.get("br", )  # None
# print(x)
# x = car.get("br", 47)  # 47
# print(x)
# y = car["br"]  # Error
# print(y)

# x = car.keys()  # Returns a list containing the dictionary's keys
# x = car.values()  # Returns a list of all the values in the dictionary

# for el in car.items(): # !!!! tuple is the answer
#     print(el)

# car.popitem()  # Removes the last inserted key-value pair
# car.pop("br")  # Removes key-value pair or Error
# car.pop("br", defaultvalue) returns defaultvalue and no Error

#
# a = ("a", "b", "c", "d")
# a = ("a", "b")
# b = ("1", "2", "3")
# x = zip(a, b)
# # print(tuple(x))
# print(x)
# print(dict(x))


# print({ch: ord(ch) for ch in input().split(',')})

# data = [("Peter", 22), ("Amy", 18), ("George", 35)]
# dict_data = {key: value for (key, value) in data}
# print(dict_data)
# print(f"{key}: {value} for (key, value) in data}") # do not work

# x = "012"
# y = "01234567"
# for i in range(len(y)):
#     j = i % len(x)
#     print(i, j, sep='->')

dict_test = {3: 4, 4: 5, 5: 5, 7: 2, 11: 2}
print(len(dict_test))
# dict_test1 = {"k3": 4, "k4": 5, "k5": 5, "k7": 2}
# sorted_dict = dict(sorted(dict_test.items(), key=lambda x: (x[1], x[0])))
# print(sorted_dict)
# sorted_dict = dict(sorted(dict_test1.items(), key=lambda x: (x[1], x[0])))
# print(sorted_dict)
# race_info = sorted(race_info, key=lambda x: -race_info[x]) # returns list with keys sorted by values

# sorted(symbols.items())  # returns list of tuples
# dict_test = dict(sorted(symbols.items()))
# for ch, count in dict_test.items():
#     print(f"{ch}: {count} time/s")
# for ch, count in sorted(dict_test.items()):
#     print(f"{ch}: {count} time/s")

# print(list(car.items()))
# print(car['model'])
