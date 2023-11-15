from unittest import TestCase, main


# class SimpleTest(unittest.TestCase):
class SimpleTest(TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    # unittest.main()
    main()
