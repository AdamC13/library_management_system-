# User: A class to represent library users with attributes like name, library ID, and a list of borrowed book titles.
class User:
    def __init__(self, name, library_id, borrowed_books):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = borrowed_books
    
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
