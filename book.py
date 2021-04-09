class Book:

    def __init__(self, author: str, title: str, publisher: str, shelf: int, category: str, subject: str):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.shelf = shelf
        self.category = category
        self.subject = subject

    def __str__(self) -> str:
        return f'Author: {self.author}, Title: {self.title}, Publisher: {self.publisher}, Shelf: {self.shelf}, ' \
               f'Category: {self.category}, Subject: {self.subject} '
