# Book: A class representing individual books with attributes such as title, author, ISBN, genre, publication date, and availability status.
class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = True

    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title
        return
    
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
        return

    def get_isbn(self):
        return self.isbn
    def set_isbn(self, isbn):
        self.isbn = isbn
        return
    
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre
        return
    
    def get_publication_date(self):
        return self.publication_date
    def set_publication_date(self, publication_date):
        self.publication_date = publication_date
        return
    
    def get_availability_status(self):
        return self.availability_status
    def set_availability_status(self, availability_status):
        self.availability_status = availability_status
        return