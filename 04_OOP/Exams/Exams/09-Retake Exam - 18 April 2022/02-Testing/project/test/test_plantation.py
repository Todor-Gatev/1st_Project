from unittest import TestCase, main
from project.plantation import Plantation


class Test(TestCase):
    def setUp(self) -> None:
        self.plant = Plantation(5)

    def test_correct_initialization(self):
        self.assertEqual(5, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_if_exists(self):
        self.plant.workers = ["asd"]
        with self.assertRaises(ValueError) as ve:
            self.plant.hire_worker("asd")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker(self):
        res = self.plant.hire_worker("asd")
        self.assertEqual(["asd"], self.plant.workers)
        self.assertEqual("asd successfully hired.", res)

    def test_len(self):
        self.plant.plants = {'a': ["as", "ad"], 'b': ["bb"]}
        self.assertEqual(3, len(self.plant))

    def test_planting_if_no_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting('a', "as")

        self.assertEqual("Worker with name a is not hired!", str(ve.exception))

    def test_planting_if_full(self):
        self.plant.workers = ['a', 'b']
        self.plant.plants = {'a': ["as", "ad", "as"], 'b': ["bb", "bc"]}
        with self.assertRaises(ValueError) as ve:
            self.plant.planting('a', "as")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_if_worker_in_plants(self):
        self.plant.workers = ['a', 'b']
        self.plant.plants = {'a': ["ad", "as"], 'b': ["bb", "bc"]}
        res = self.plant.planting('a', "as")

        self.assertEqual("a planted as.", res)
        self.assertEqual({'a': ["ad", "as", "as"], 'b': ["bb", "bc"]}, self.plant.plants)

    def test_planting_if_worker_not_in_plants(self):
        self.plant.workers = ['a', 'b']
        self.plant.plants = {'b': ["bb", "bc"]}
        res = self.plant.planting('a', "as")

        self.assertEqual("a planted it's first as.", res)
        self.assertEqual({'b': ["bb", "bc"], 'a': ["as"]}, self.plant.plants)

    def test_str(self):
        self.plant.workers = ['a', 'b']
        self.plant.plants = {'a': ["ad", "as"], 'b': ["bb", "bc"]}
        expected = ("Plantation size: 5\n"
                    "a, b\n"
                    "a planted: ad, as\n"
                    "b planted: bb, bc")

        self.assertEqual(expected, str(self.plant))

    def test_repr(self):
        self.plant.workers = ['a', 'b']
        self.plant.plants = {'a': ["ad", "as"], 'b': ["bb", "bc"]}
        expected = ("Size: 5\n"
                    "Workers: a, b")

        self.assertEqual(expected, repr(self.plant))


if __name__ == "__main__":
    main()
