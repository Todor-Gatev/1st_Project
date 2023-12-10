from typing import Any, NamedTuple


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._array = capacity * [None]

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError("Capacity must be greater than zero")
        self.__capacity = value

    @property
    def array(self):
        return [pair for pair in self._array if pair]

    def hash(self, key):
        return hash(key) % self.capacity

    def __len__(self):
        return len(self.array)

    def __setitem__(self, key, value):
        self._array[self.hash(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._array[self.hash(key)]
        if not pair:
            raise KeyError(key)

        return pair.value


# print(hash("hey"))
# print(hash("he"))
