from unittest import TestCase, main

from project.car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("Merc", "SLR", 12, 72)

    def test_correct_initialization(self):
        self.assertEqual("Merc", self.car.make)
        self.assertEqual("SLR", self.car.model)
        self.assertEqual(12, self.car.fuel_consumption)
        self.assertEqual(72, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_make_is_empty_str_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_is_empty_str_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_zero_or_negative_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_zero_or_negative_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_is_negative_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_fuel_value_is_zero_or_negative_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_fuel_is_added_to_fuel_amount(self):
        self.car.refuel(12)

        self.assertEqual(12, self.car.fuel_amount)

    def test_refuel_if_fuel_value_and_fuel_amount_are_greater_than_fuel_capacity(self):
        self.car.refuel(1 + self.car.fuel_capacity)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_if_fuel_value_is_less_than_needed_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = 11
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_if_fuel_amount_is_decreased_correct(self):
        self.car.fuel_amount = 12
        self.car.drive(100)

        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    main()
