from typing import List, Dict

from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # {author: [books]}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str or None:
        if author in self.books_available:
            if book_name in self.books_available[author]:
                self.books_available[author].remove(book_name)

                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}

                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)

                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for u in self.rented_books:
            if book_name in self.rented_books[u]:
                return (f'The book "{book_name}" is already rented and '
                        f'will be available in {self.rented_books[u][book_name]} days!')

    def return_book(self, author: str, book_name: str, user: User) -> str or None:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"

        del self.rented_books[user.username][book_name]
        self.books_available[author].append(book_name)
        user.books.remove(book_name)
