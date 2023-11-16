from unittest import TestCase, main

from project.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Asd")

    def test_initialization(self):
        self.assertEqual("Asd", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_raise_exception_when_eat_with_fed_status_true(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_valid_eat(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_raise_exception_when_sleep_with_fed_status_false(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleepy_state_to_be_false_after_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
