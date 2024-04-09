# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
from random import getrandbits
class User:
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.library_id = str(getrandbits(10000))
        self.borrowed_books = []
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return
    
    def get_library_id(self):
        return self.library_id
    def set_library_id(self, library_id):
        self.library_id = library_id
        return

    def get_borrowed_books(self):
        return self.borrowed_books
    def set_borrowed_books(self, borrowed_books):
        self.borrowed_books = borrowed_books
        return
    def append_borrowed_book(self, book):
        self.borrowed_books.append(book)
    def remove_borrowed_book(self, book):
        self.borrowed_books.remove(book)

    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
        return