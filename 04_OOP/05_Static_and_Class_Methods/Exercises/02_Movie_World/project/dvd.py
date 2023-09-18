class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        number_to_month = {1: "January", 2: "February", 3: "March", 4: "April",
                           5: "May", 6: "June", 7: "July", 8: "August",
                           9: "September", 10: "October", 11: "November", 12: "December"}
        # from calendar import month_name -> month_name[int] returns month name

        return cls(name, dvd_id, int(year), number_to_month[int(month)], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

# d2 = DVD.from_date(2, "The Cds 2", "23.12.2020", 3)
# print(str(d2))
