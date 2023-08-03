def age_assignment(*args, **kwargs):
    names = list(args)
    names.sort()

    return "\n".join(f"{name} is {kwargs[name[0]]} years old." for name in names)


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))
