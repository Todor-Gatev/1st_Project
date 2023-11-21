from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class Test(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("asd", 23, 12.5)

    def test_correct_initialization(self):
        self.assertEqual("asd", self.player.name)
        self.assertEqual(23, self.player.age)
        self.assertEqual(12.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "as"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_if_tour_exists(self):
        self.player.wins = ["a"]
        expected = "a has been already added to the list of wins!"
        res = self.player.add_new_win("a")

        self.assertEqual(expected, res)

    def test_add_new_win_(self):
        self.player.add_new_win("a")
        self.assertEqual(["a"], self.player.wins)

    def test_lt_if_points_less_than_other(self):
        other = TennisPlayer("bbb", 23, 23)
        expected = "bbb is a top seeded player and he/she is better than asd"
        res = self.player.__lt__(other)

        self.assertEqual(expected, res)

    def test_lt_if_points(self):
        other = TennisPlayer("bbb", 23, 12.5)
        expected = "asd is a better player than bbb"
        res = self.player.__lt__(other)

        self.assertEqual(expected, res)

    def test_str(self):
        self.player.wins = ["a", "b"]
        expected = ("Tennis Player: asd\n"
                    "Age: 23\n"
                    "Points: 12.5\n"
                    "Tournaments won: a, b")

        self.assertEqual(expected, self.player.__str__())


if __name__ == "__main__":
    main()
