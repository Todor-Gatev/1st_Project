from project.library import Library
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.library = Library("asd")

    def test_correct_initialization(self):
        self.assertEqual("asd", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_if_new_author(self):
        self.library.add_book('a', 'aa')

        self.assertEqual({'a': ['aa']}, self.library.books_by_authors)

    def test_add_book_if_new_book(self):
        self.library.books_by_authors = {'a': ['bb']}
        self.library.add_book('a', 'aa')

        self.assertEqual({'a': ['bb', 'aa']}, self.library.books_by_authors)

    def test_add_book_if_existing_author_and_book(self):
        self.library.books_by_authors = {'a': ['bb', 'aa']}
        self.library.add_book('a', 'aa')

        self.assertEqual({'a': ['bb', 'aa']}, self.library.books_by_authors)

    def test_add_new_reader(self):
        self.library.add_reader("Ali")

        self.assertEqual({"Ali": []}, self.library.readers)

    def test_add_existing_reader(self):
        self.library.readers = {"Ali": []}
        res = self.library.add_reader("Ali")
        expected = "Ali is already registered in the asd library."

        self.assertEqual(expected, res)

    def test_rent_book_if_not_reader(self):
        self.library.books_by_authors = {'a': ['bb', 'aa']}
        self.library.readers = {"Ali": []}
        res = self.library.rent_book("Solo", 's', 'as')
        expected = "Solo is not registered in the asd Library."

        self.assertEqual(expected, res)

    def test_rent_book_if_not_author(self):
        self.library.books_by_authors = {'a': ['bb', 'aa']}
        self.library.readers = {"Ali": []}
        res = self.library.rent_book("Ali", 'as', 'aas')
        expected = "asd Library does not have any as's books."

        self.assertEqual(expected, res)

    def test_rent_book_if_not_title(self):
        self.library.books_by_authors = {'as': ['bb', 'aa']}
        self.library.readers = {"Ali": []}
        res = self.library.rent_book("Ali", 'as', 'aas')
        expected = """asd Library does not have as's "aas"."""

        self.assertEqual(expected, res)

    def test_rent_book_if_all_ok(self):
        self.library.books_by_authors = {'as': ['bb', 'aa']}
        self.library.readers = {"Ali": [{"bbb": "fff"}]}
        self.library.rent_book("Ali", 'as', 'aa')

        self.assertEqual({'as': ['bb']}, self.library.books_by_authors)
        self.assertEqual({"Ali": [{"bbb": "fff"}, {"as": "aa"}]}, self.library.readers)


if __name__ == "__main__":
    main()
