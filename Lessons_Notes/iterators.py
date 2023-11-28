my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))

class MyIterator:
    def __init__(self, start=0, end=3):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1

        raise StopIteration


my_iterator = MyIterator()

for num in my_iterator:
    print(num, ' ')


