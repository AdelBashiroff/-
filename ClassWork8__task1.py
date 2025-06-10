class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Название: {self.title}, Автор: {self.author}, Год: {self.year}'
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f'Книга {book.title} успешно добавлена')
        else:
            print('Можно добавлять только объекты класса Book')

    def find_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        return found_books

    def find_books_by_year(self, year):
        found_books = []
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        return found_books

library = Library()
book1 = Book('Герой Нашего Времени', 'Михаил Лермонтов', 1840)
book2 = Book('Преступление и Наказание', 'Федор Достоевский', 1866)

library.add_book(book1)
library.add_book(book2)

books = library.find_books_by_author('Федор Достоевский')
for book in books:
    print(book)
