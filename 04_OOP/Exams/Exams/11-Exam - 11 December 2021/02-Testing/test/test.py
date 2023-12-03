from project.team import Team

from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.team = Team("asd")

    def test_correct_initialization(self):
        self.assertEqual("asd", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "1asd"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member(self):
        self.team.members = {'c': 7}
        names_ages = {'a': 1, 'b': 2, 'c': 3}
        res = self.team.add_member(**names_ages)
        expected = {'a': 1, 'b': 2, 'c': 7}
        expected1 = "Successfully added: a, b"

        self.assertEqual(expected, self.team.members)
        self.assertEqual(expected1, res)

    def test_add_member1(self):
        self.team.members = {'c': 7}
        names_ages = {'c': 3}
        res = self.team.add_member(**names_ages)
        expected = {'c': 7}
        expected1 = "Successfully added: "

        self.assertEqual(expected, self.team.members)
        self.assertEqual(expected1, res)

    def test_remove_member_if_not_member(self):
        self.team.members = {'c': 7}
        res = self.team.remove_member('a')
        expected = "Member with name a does not exist"

        self.assertEqual(expected, res)

    def test_remove_member(self):
        self.team.members = {'c': 7, 'a': 1}
        res = self.team.remove_member('a')
        expected = "Member a removed"

        self.assertEqual(expected, res)
        self.assertEqual({'c': 7}, self.team.members)

    def test_gt_with_more_members(self):
        self.team.members = {'c': 7, 'a': 1, 'd': 3}
        other = Team("other")
        other.members = {'c': 7, 'd': 12}

        self.assertEqual(True,  self.team.__gt__(other))

    def test_gt_with_equal_num_of_members(self):
        self.team.members = {'a': 1}
        other = Team("other")
        other.members = {'c': 7}

        self.assertFalse(self.team.__gt__(other))

    def test_gt_with_less_num_of_members(self):
        self.team.members = {'a': 1}
        other = Team("other")
        other.members = {'c': 7, 'b': 4}

        self.assertFalse(self.team.__gt__(other))

    def test_add(self):
        self.team.members = {'c': 7, 'a': 1}
        other = Team("other")
        other.members = {'c': 7, 'b': 2}
        new = self.team.__add__(other)

        self.assertEqual("asdother", new.name)
        self.assertEqual({'c': 7, 'a': 1, 'b': 2}, new.members)

    def test_len(self):
        self.team.members = {'c': 7, 'a': 1}

        self.assertEqual(2, len(self.team))

    def test_str(self):
        self.team.members = {'c': 7, 'a': 1, 'd': 5, 'b': 7}
        expected = ("Team name: asd\n"
                    "Member: b - 7-years old\n"
                    "Member: c - 7-years old\n"
                    "Member: d - 5-years old\n"
                    "Member: a - 1-years old")

        self.assertEqual(expected, str(self.team))


if __name__ == "__main__":
    main()
