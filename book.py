class Book:

    def __init__(self, author: str, title: str, publisher: str, shelf: int, category: str, subject: str):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.shelf = shelf
        self.category = category
        self.subject = subject

    def __str__(self) -> str:
        return f'\u001b[32;1mAuthor\u001b[0m: {self.author}, \u001b[32;1mTitle\u001b[0m: {self.title}, \u001b[' \
               f'32;1mPublisher\u001b[0m: {self.publisher}, \u001b[32;1mShelf\u001b[0m: {self.shelf}, ' \
               f'\u001b[32;1mCategory\u001b[0m: {self.category}, \u001b[32;1mSubject\u001b[0m: {self.subject} '

