print(isinstance(11, float))  # False
print(isinstance(11.0, int))  # False
print(isinstance(11, float) or isinstance(11, int))  # True
print(isinstance(11.0, float) or isinstance(11.0, int))  # True
