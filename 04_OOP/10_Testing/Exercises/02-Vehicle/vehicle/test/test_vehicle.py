from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(41.5, 111.2)

    def test_default_consumption_class_attribute_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(41.5, self.vehicle.fuel)
        self.assertEqual(41.5, self.vehicle.capacity)
        self.assertEqual(111.2, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel_expected_exception(self):
        self.vehicle.fuel = 12

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_fuel_decreases_correct(self):
        self.vehicle.drive(2)

        self.assertEqual(39, self.vehicle.fuel)

    def test_refuel_too_much_fuel_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(0.1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correct_fuel_added(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1)

        self.assertEqual(2, self.vehicle.fuel)

    def test_correct_str_method(self):
        expected = ("The vehicle has 111.2 horse power"
                    " with 41.5 fuel left "
                    "and 1.25 fuel consumption")

        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    main()
