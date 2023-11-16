# import unittest
from unittest import TestCase, main


# class SimpleTest(unittest.TestCase):
class SimpleTest(TestCase):
    def test_upper(self):
        string = 'foo'  # arrange
        result = string.upper()  # act
        expected_result = 'FOOa'
        self.assertEqual(expected_result, result)  # assert


if __name__ == '__main__':
    # unittest.main()
    main()

# region Error
# Traceback (most recent call last):
#   File "C:\Users\Happy\AppData\Local\Programs\PyCharm Community\plugins
#   \python-ce\helpers\pycharm\_jb_unittest_runner.py", line 38, in <module>
#     sys.exit(main(argv=args, module=None, testRunner=unittestpy.TeamcityTestRunner,
# car = Car("a", "b", 1, 4) - remove
# car.make = ""- remove
# print(car) - remove
# endregion


# self.assertEqual(False, self.cat.fed)  self.assertFalse(self.cat.fed)

# class PersonTests(TestCase):
#     def setUp(self):  # it’s part of unittest.TestCase
#         self.person = Person("Luc", "Peterson", 25)  # arrange
