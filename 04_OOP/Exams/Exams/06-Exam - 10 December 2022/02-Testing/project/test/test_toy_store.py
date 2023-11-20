from unittest import TestCase, main
from project.toy_store import ToyStore


class Test(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_initialization(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_if_not_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('w', 'a')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_if_toy_on_shelf(self):
        self.store.toy_shelf['A'] = 'a'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'a')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_if_shelf_is_taken(self):
        self.store.toy_shelf['A'] = 'a'
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'b')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy(self):
        res = self.store.add_toy('A', 'a')
        expected = self.toy_shelf = {
            "A": 'a',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual("Toy:a placed successfully!", res)
        self.assertEqual(expected, self.store.toy_shelf)

    def test_remove_toy_if_not_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('z', 'a')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_if_wrong_toy(self):
        self.store.toy_shelf['A'] = 'va'
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'a')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy(self):
        self.store.toy_shelf['A'] = 'a'
        res = self.store.remove_toy('A', 'a')
        expected = self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual("Remove toy:a successfully!", res)
        self.assertEqual(expected, self.store.toy_shelf)


if __name__ == "__main__":
    main()
