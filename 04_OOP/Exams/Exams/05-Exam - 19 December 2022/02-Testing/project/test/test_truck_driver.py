from project.truck_driver import TruckDriver

from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("asd", 12.5)

    def test_correct_initialization(self):
        self.assertEqual("asd", self.driver.name)
        self.assertEqual(12.5, self.driver.money_per_mile)
        self.driver.available_cargos = {}
        self.driver.earned_money = 0
        self.driver.miles = 0

    def test_earned_money_settings(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -0.1

        self.assertEqual("asd went bankrupt.", str(ve.exception))

    def test_add_cargo_if_cargo_is_added(self):
        self.driver.available_cargos = {'a': 10}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('a', 10)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo(self):
        res = self.driver.add_cargo_offer('a', 10)
        expected = "Cargo for 10 to a was added as an offer."

        self.assertEqual(expected, res)
        self.assertEqual({'a': 10}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_if_not_cargo(self):
        res = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", res)

    def test_drive_best_cargo_with_cargo(self):
        self.driver.available_cargos = {'a': 9, 'b': 10_000}
        res = self.driver.drive_best_cargo_offer()
        expected = "asd is driving 10000 to b."

        self.assertEqual(expected, res)
        self.assertEqual(10000, self.driver.miles)
        self.assertEqual(113250, self.driver.earned_money)

    def test_check_for_activities(self):
        self.driver.earned_money = 11750
        self.driver.check_for_activities(10000)

        self.assertEqual(0, self.driver.earned_money)

    def test_eat(self):
        self.driver.earned_money = 20
        self.driver.eat(250)

        self.assertEqual(0, self.driver.earned_money)

    def test_sleap(self):
        self.driver.earned_money = 45
        self.driver.sleep(1000)

        self.assertEqual(0, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.earned_money = 500
        self.driver.pump_gas(1500)

        self.assertEqual(0, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.earned_money = 7500
        self.driver.repair_truck(10000)

        self.assertEqual(0, self.driver.earned_money)

    def test_repr(self):
        expected = "asd has 0 miles behind his back."
        res = self.driver.__repr__()

        self.assertEqual(expected, res)


if __name__ == "__main__":
    main()
