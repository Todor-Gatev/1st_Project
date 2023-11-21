from unittest import TestCase, main
from project.robot import Robot


class Test(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("1", "Military", 3, 100.00)

    def test_default_class_attributes_are_correct(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(3, self.robot.available_capacity)
        self.assertEqual(100.00, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "asd"

        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        self.assertEqual(expected, str(ve.exception))

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -0.1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_if_hardware_component_exists(self):
        expected = "Robot 1 was not upgraded."
        self.robot.hardware_upgrades = ["ram"]

        self.assertEqual(expected, self.robot.upgrade("ram", 1))

    def test_upgrade_new_component(self):
        res = self.robot.upgrade("ram", 1)
        expected = 'Robot 1 was upgraded with ram.'
        self.assertEqual(101.5, self.robot.price)
        self.assertEqual(["ram"], self.robot.hardware_upgrades)
        self.assertEqual(expected, res)

    def test_update_if_not_capacity(self):
        expected = "Robot 1 was not updated."
        res = self.robot.update(1, 4)

        self.assertEqual(expected, res)

    def test_update_if_old_version(self):
        expected = "Robot 1 was not updated."
        self.robot.software_updates = [1]
        res = self.robot.update(1, 3)

        self.assertEqual(expected, res)

    def test_update(self):
        expected = "Robot 1 was updated to version 1."
        res = self.robot.update(1, 3)

        self.assertEqual(0, self.robot.available_capacity)
        self.assertEqual([1], self.robot.software_updates)
        self.assertEqual(expected, res)

    def test_gt_if_price_bigger_then_other(self):
        other = Robot("3", "Military", 3, 99.99)
        expected = "Robot with ID 1 is more expensive than Robot with ID 3."

        self.assertEqual(expected, self.robot.__gt__(other))

    def test_gt_if_price_equal_then_other(self):
        other = Robot("3", "Military", 3, 100.00)
        expected = "Robot with ID 1 costs equal to Robot with ID 3."

        self.assertEqual(expected, self.robot.__gt__(other))

    def test_gt_if_price_is_less_then_other(self):
        other = Robot("3", "Military", 3, 100.01)
        expected = "Robot with ID 1 is cheaper than Robot with ID 3."

        self.assertEqual(expected, self.robot.__gt__(other))


if __name__ == "__main__":
    main()
