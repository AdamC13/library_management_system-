# Author: A class representing book authors with attributes like name and biography.
class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
        self.books = []

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return
    
    def get_biography(self):
        return self.biography
    def set_biography(self, biography):
        self.biography = biography
        return
    
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        self.books.remove(book)
    def get_books(self):
        return self.books
    
