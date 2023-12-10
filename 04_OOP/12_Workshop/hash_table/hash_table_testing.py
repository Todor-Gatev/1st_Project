from unittest import TestCase, main
from hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self):
        self.hash_table = HashTable(100)
        self.hash_table["Hello"] = "Hellow World!"
        self.hash_table[7.2] = 12
        self.hash_table[False] = True

    def test_create_hash_table(self):
        self.assertIsNotNone(HashTable(3))

    def test_capacity(self):
        self.assertEqual(3, len(self.hash_table.array))




if __name__ == '__main__':
    main()
