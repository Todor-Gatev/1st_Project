def get_data_type(str_a, str_b):
    if str_a == "int":
        return int(str_b) * 2
    elif str_a == "real":
        return f"{(float(str_b) * 1.5):.2f}"
    elif str_a == "string":
        return f"${str_b}$"


data_type = input()
user_data = input()

print(get_data_type(data_type, user_data))
