from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class Test(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("aaaa")
        self.station.arrival_trains = deque(['a', 'b'])
        self.station.departure_trains = deque(['f', 'g'])

    def test_correct_initialization(self):
        self.assertEqual("aaaa", self.station.name)
        self.assertEqual(deque(['a', 'b']), self.station.arrival_trains)
        self.assertEqual(deque(['f', 'g']), self.station.departure_trains)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "asd"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board('c')

        self.assertEqual(deque(['a', 'b', 'c']), self.station.arrival_trains)

    def test_train_has_arrived_if_not_his_turn(self):
        res = self.station.train_has_arrived('b')
        expected = "There are other trains to arrive before b."

        self.assertEqual(expected, res)

    def test_train_has_arrived_if_his_turn(self):
        res = self.station.train_has_arrived('a')
        expected = "a is on the platform and will leave in 5 minutes."

        self.assertEqual(expected, res)
        self.assertEqual(deque(['b']), self.station.arrival_trains)
        self.assertEqual(deque(['f', 'g', 'a']), self.station.departure_trains)

    def test_train_has_left_if_not_departures(self):
        self.station.departure_trains = deque()
        self.assertFalse(self.station.train_has_left('w'))

    def test_train_has_left_if_not_his_turn(self):
        self.assertFalse(self.station.train_has_left('g'))

    def test_train_has_left(self):
        self.assertTrue(self.station.train_has_left('f'))
        self.assertEqual(deque(['g']), self.station.departure_trains)

if __name__ == "__main__":
    main()






