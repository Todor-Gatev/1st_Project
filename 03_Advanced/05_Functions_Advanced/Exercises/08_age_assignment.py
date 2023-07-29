def age_assignment(*args, **kwargs):
    names = sorted(args)
    ch_ages = sorted(kwargs.items())

    return "\n".join(f"{names[idx]} is {ch_ages[idx][1]} years old." for idx in range(len(names)))


# print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
