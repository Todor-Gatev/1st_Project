from project.movie import Movie
from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("asd", 2001, 1.2)

    def test_correct_initialization(self):
        self.assertEqual("asd", self.movie.name)
        self.assertEqual(2001, self.movie.year)
        self.assertEqual(1.2, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_if_exists(self):
        self.movie.actors = ['a']
        res = self.movie.add_actor('a')

        self.assertEqual("a is already added in the list of actors!", res)

    def test_add_actor(self):
        self.movie.add_actor('a')

        self.assertEqual(['a'], self.movie.actors)

    def test_gt_if_bigger(self):
        other = Movie("asd1", 2001, 1.1)
        expected = '"asd" is better than "asd1"'
        res = self.movie.__gt__(other)

        self.assertEqual(expected, res)

    def test_gt(self):
        other = Movie("asd1", 2001, 1.2)
        expected = '"asd1" is better than "asd"'
        res = self.movie.__gt__(other)

        self.assertEqual(expected, res)

    def test_repr(self):
        self.movie.actors = ['a', 'b', 'c']
        expected = ("Name: asd\n"
                    "Year of Release: 2001\n"
                    "Rating: 1.20\n"
                    "Cast: a, b, c")

        self.assertEqual(expected, repr(self.movie))


if __name__ == "__main__":
    main()
