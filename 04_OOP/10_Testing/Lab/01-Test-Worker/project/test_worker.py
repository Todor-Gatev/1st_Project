from unittest import TestCase, main

from project.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Adam", 1112, 111)

    def test_initialization(self):
        self.assertEqual("Adam", self.worker.name)
        self.assertEqual(1112, self.worker.salary)
        self.assertEqual(111, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_worker_money_when_working(self):
        self.worker.work()
        self.assertEqual(1112, self.worker.money)

    def test_decrease_worker_energy_when_working(self):
        self.worker.work()
        self.assertEqual(110, self.worker.energy)

    def test_raise_exception_when_worker_working_with_zero_or_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_worker_energy_with_one_after_rest(self):
        self.worker.rest()
        self.assertEqual(112, self.worker.energy)

    def test_get_correct_info(self):
        self.assertEqual("Adam has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
