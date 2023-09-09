from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # {autor: [books]}
        self.rented_books: Dict[str: Dict[str: int]] = {}  # {usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)

                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}

                self.rented_books[user.username][book_name] = days_to_return

                return f"{book_name} successfully rented for the next {days_to_return} days!"

            for username in self.rented_books:
                if book_name in self.rented_books[username]:
                    will_be_available = self.rented_books[username][book_name]

                    return (f'The book "{book_name}" is already rented and'
                            f' will be available in {will_be_available} days!')

    def return_book(self, author: str, book_name: str, user: User) -> str or None:
        if book_name in user.books:
            user.books.remove(book_name)
            self.rented_books[user.username].pop(book_name)
            # del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)

        else:
            return f"{user.username} doesn't have this book in his/her records!"


# user = User(12, 'George')
# library = Library()
# library.user_records.append(user)
#
# [print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]
#
# library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
#                                                 'The Prisoner of Azkaban',
#                                                 'The Goblet of Fire',
#                                                 'The Order of the Phoenix',
#                                                 'The Half-Blood Prince',
#                                                 'The Deathly Hallows']})
# library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
# print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
# print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
# library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
# print(library.books_available)
# print(library.rented_books)
# print(user.books)
