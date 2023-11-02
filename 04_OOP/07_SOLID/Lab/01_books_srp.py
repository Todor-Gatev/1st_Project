from typing import List


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def find_book(self, book_title) -> (Book, str):
        try:
            return [b for b in self.books if b.title == book_title]
        except IndexError:
            return "no book"
