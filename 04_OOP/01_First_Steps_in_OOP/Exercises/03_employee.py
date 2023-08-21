class Employee:
    MONTHS = 12

    def __init__(self, employee_id: int, first_name: str, last_name: str, salary: int):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, amount: int):
        self.salary += amount

        return self.salary

    def get_annual_salary(self):
        return self.salary * Employee.MONTHS
        # return self.salary * self.MONTHS
        # return self.salary * 12


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        e = Employee(123, "A", "B", 1500)
        self.assertEqual(e.id, 123)
        self.assertEqual(e.first_name, "A")
        self.assertEqual(e.last_name, "B")
        self.assertEqual(e.salary, 1500)

    def test_get_full_name(self):
        e = Employee(3333, "C", "B", 400)
        res = e.get_full_name()
        self.assertEqual(res, "C B")

    def test_get_annual_salary(self):
        e = Employee(234155, "NC", "NFD", 4000)
        res = e.get_annual_salary()
        self.assertEqual(res, 48000)

    def test_raise_salary(self):
        e = Employee(1, "1", "2", 1)
        res = e.raise_salary(199)
        self.assertEqual(res, 200)
        self.assertEqual(e.salary, 200)


if __name__ == "__main__":
    unittest.main()
