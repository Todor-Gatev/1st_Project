from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class Test(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("asd", "ddd", 1000, 500.00)

    def test_correct_initialization(self):
        self.assertEqual("asd", self.car.model)
        self.assertEqual("ddd", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(500.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promo_price_if_new_is_bigger(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(501)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price(self):
        res = self.car.set_promotional_price(111)

        self.assertEqual(111, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', res)

    def test_need_repair_if_high_price(self):
        res = self.car.need_repair(250.1, "pump")

        self.assertEqual('Repair is impossible!', res)

    def test_need_repair(self):
        res = self.car.need_repair(250, "pump")
        expected = 'Price has been increased due to repair charges.'

        self.assertEqual(750, self.car.price)
        self.assertEqual(["pump"], self.car.repairs)
        self.assertEqual(expected, res)

    def test_gt_if_diff_types(self):
        other = SecondHandCar("b", "g", 1000, 500)

        res = self.car.__gt__(other)

        self.assertEqual('Cars cannot be compared. Type mismatch!', res)

    def test_gt_same_types(self):
        other = SecondHandCar("b", "ddd", 1000, 500)
        res = self.car.__gt__(other)

        self.assertFalse(res)

        other = SecondHandCar("b", "ddd", 1000, 499.99)
        res = self.car.__gt__(other)

        self.assertTrue(res)

    def test_str(self):
        expected = ("Model asd | Type ddd | Milage 1000km\n"
                    "Current price: 500.00 | Number of Repairs: 0")

        self.assertEqual(expected, self.car.__str__())


if __name__ == "__main__":
    main()
