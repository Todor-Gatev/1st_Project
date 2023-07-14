# Read user input
wanted_book = input()

# Logic
current_book = ''
book_counter = 0

while True:
    current_book = input()
    if current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    if current_book == wanted_book:
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1

# Print Output

# while wanted_book != current_book:
#     current_book = input()
#     if current_book == 'No More Books':
#         print('The book you search is not here!')
#         print(f'You checked {book_counter} books.')
#         break
#
#     book_counter += 1
#
# else:
#     book_counter -= 1
#     print(f'You checked {book_counter} books and found it.')
