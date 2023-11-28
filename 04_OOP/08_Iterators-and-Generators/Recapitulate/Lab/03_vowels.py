class vowels:
    VOWELS = "AaEeIiOoUu"

    def __init__(self, text):
        self.text = text
        self.found_vowels = [ch for ch in self.text if ch in self.VOWELS]
        self.end = len(self.found_vowels)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.end:
            self.i += 1

            # if self.text[self.i - 1] in self.VOWELS:
            #     return self.text[self.i - 1]

            # continue

            return self.found_vowels[self.i - 1]

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
