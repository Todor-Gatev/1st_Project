from unittest import TestCase, main

from project.integer_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList("12", False, 2.3, 1, 2, 3)

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_correct_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_invalid_value_expected_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("a")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_with_valid_value(self):
        result = self.integer_list.add(7)  # we are testing return

        self.assertEqual([1, 2, 3, 7], result)
        # self.assertEqual([1, 2, 3, 7], self.integer_list._IntegerList__data)

    def test_remove_index_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index(self):
        result = self.integer_list.remove_index(1)

        self.assertEqual(2, result)
        self.assertNotIn(2, self.integer_list._IntegerList__data)

    def test_get_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_insert_with_invalid_index_expected_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(3, 7)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_invalid_el_value_expected_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, '7')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_el_and_index(self):
        self.integer_list.insert(1, 7)

        # self.assertEqual([1, 7, 2, 3], self.integer_list._IntegerList__data)
        self.assertIn(7, self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual(3, self.integer_list.get_biggest())
        # self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_get_index(self):
        self.assertEqual(0, self.integer_list.get_index(1))


if __name__ == "__main__":
    main()
