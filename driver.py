from os import system
from classes.author import Author
from classes.user import User
from classes import books 

library = {'books': [], 'authors': [], 'users': []}

#<====================> Main Menu <====================>

def main():
    while True:
        system('cls')
        action = input('''

Welcome to the Library Management System!

Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Select an option: 
'''
        )

        if action == '1':
            book_operations()
        elif action == '2':
            user_operations()
        elif action == '3':
            author_operations()
        elif action == '4':
            break
        else:
            print("Invalid input! ")

#<====================> Book Operations <====================>

def book_operations():
    system('cls')
    user_input = input('''
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to Main Menu
                           
Select an option: 
'''
)
    
#    <----------> Adding a new book <---------->

    if user_input == '1':

#        ---------- Getting Book Values ----------

        title = input("\nWhat is the title of the book you will be adding? ")
        author = input(f"\nWhat is the author of {title}? ")
        isbn = input(f"\nWhat is the isbn of {title}? ")
        genre = input(f"\nWhat is the genre of {title}? ")
        publication_date = input(f"\nWhat is the publication date of {title}? ")

#        ---------- Adding the appropriate object to the library ----------

        if genre.lower() == 'fantasy':
            book_obj = books.FantasyBook(title, author, isbn, publication_date)
            library['books'].append(book_obj)
        
        elif genre.lower() == 'fiction':
            book_obj = books.FictionBook(title, author, isbn, publication_date)
            library['books'].append(book_obj)
        
        elif genre.lower() == 'mystery':
            book_obj = books.MysteryBook(title, author, isbn, publication_date)
            library['books'].append(book_obj)
        
        elif genre.lower() == 'nonfiction':
            book_obj = books.NonFictionBook(title, author, isbn, publication_date)
            library['books'].append(book_obj)
        
        elif genre.lower() == 'sciencefiction':
            book_obj = books.ScienceFictionBook(title, author, isbn, publication_date)
            library['books'].append(book_obj)
        
        else:
            book_obj = books.Book(title, author, isbn, genre, publication_date)
            library['books'].append(book_obj)
        
        print(library)
        input("")
    
#    <----------> Borrowing a book <---------->

    if user_input == '2':

#        ---------- Finding the book ----------

        name = input("\nWhat is the name of the book you would like to borrow? ")
        username = input("\nWhat is your username? ")
        
        for book in library['books']:
            if book.title == name:
                
#                --- Checking if the found book is available ---

                if book.get_availability_status():
                    book.set_availability_status(False)
                    input(f"\n'{name}' has been checked out, enjoy your book! ")
                    return
                else:
                    input(f"\nSorry '{name}' is already checked out. ")
                    return
            
        input(f"\nSorry we do not have '{name}'. ")


#    <----------> Returning a book <---------->

    if user_input == '3':

#        ---------- Finding the book ----------

        name = input("\nWhat is the name of the book you would like to return? ")
        username = input("\nWhat is your username? ")
        
        for book in library['books']:
            if book.title == name:
                
#                --- Checking if the found book is in the library ---

                if not book.get_availability_status():
                    book.set_availability_status(True)
                    input(f"\n'{name}' has been returned, time to read another book! ")
                    return
                else:
                    input(f"\n'{name}' has already been returned. ")
                    return
                
            # If book is not found
        input(f"\nSorry we cannot find '{name}'. Try checking the books you have checked out with the user operations menu. ")

#    <----------> Searching for a book <---------->

    if user_input == '4':

#        ---------- Finding the book ----------

        name = input("\nWhat is the name of the book you are looking for? ")

        for book in library['books']:
            if book.title == name:

#                --- Showing the details of the book ---

                print(f'''

{book.get_title()} by {book.get_author()}.

{book.get_title()} is a {book.get_genre()} book, published on {book.get_publication_date()}

                      ''')
                if book.get_availability_status():
                    input(f"'{name}' is currently available for checkout! ")
                    return
                else:
                    input(f"'{name}' is currently unavailable for checkout. ")
                    return
            
            # If book is not found
        input(f"\nSorry, '{name}' could not be found in the library. ")

#    <----------> Displaying all books <---------->

    if user_input == '5':
        print('\n')
        for book in library['books']:
            print(f"{book.get_title()}")
        
        input("\n")


#<====================> User Operations <====================>

def user_operations():
    system('cls')
    user_input = input('''
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Back to Main Menu
                       
Select an option: 
'''
)


#<====================> Author Operations <====================>

def author_operations():
    system('cls')
    user_input = input('''
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Back to Main Menu
                       
Select an option: 
'''
)


#<====================> Function Calls <====================>

main()