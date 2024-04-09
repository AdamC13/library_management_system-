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

        for auth in library['authors']: #checking for the author in our library
            if auth.get_name() == author:

                if genre.lower() == 'fantasy':
                    book_obj = books.FantasyBook(title, author, isbn, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)
                
                elif genre.lower() == 'fiction':
                    book_obj = books.FictionBook(title, author, isbn, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)

                elif genre.lower() == 'mystery':
                    book_obj = books.MysteryBook(title, author, isbn, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)
                
                elif genre.lower() == 'nonfiction':
                    book_obj = books.NonFictionBook(title, author, isbn, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)
                
                elif genre.lower() == 'sciencefiction':
                    book_obj = books.ScienceFictionBook(title, author, isbn, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)
                
                else:
                    book_obj = books.Book(title, author, isbn, genre, publication_date)
                    library['books'].append(book_obj)
                    auth.add_book(book_obj)
            break
                
        else:
            print(f"Sorry {author} is not an Auhtor in our library, please add the author first.")
        
        input("The book was added succesfully! ")
    
#    <----------> Borrowing a book <---------->

    if user_input == '2':

#        ---------- Finding the book ----------
        title = input("\nWhat is the name of the book you would like to borrow? ")
        username = input("\nWhat is your username? ")
        
        username_in_library = False
        for user in library['users']:
            if user.get_username() == username:
                username_in_library = True

        
        if username_in_library:
            for book in library['books']:
                if book.title == title:
                    
    #               --- Checking if the found book is available ---
                    if book.get_availability_status():
                        book.set_availability_status(False)
                        
                        for user in library['users']:
                            if user.get_username() == username:
                                user.append_borrowed_book(book)


                        input(f"\n'{title}' has been checked out, enjoy your book! ")
                        return
                    else:
                        input(f"\nSorry '{title}' is already checked out. ")
                        return
            else:
                input(f"\nSorry we do not have '{title}'. ")
                return
        else:
            input(f"Sorry {username} is not a registered user.")
            return

                


#    <----------> Returning a book <---------->

    if user_input == '3':

#        ---------- Finding the book ----------
        title = input("\nWhat is the name of the book you would like to return? ")
        username = input("\nWhat is your username? ")

        
        
        for user in library['users']:
            if user.get_username() == username:
                # if title in user.get_borrowed_books():
                #     user.remove_borrowed_book(title)

                for book in library['books']:
                    if book.title == title:
                        
#                       --- Checking if the found book is in the library ---
                        if not book.get_availability_status() and book in user.get_borrowed_books():
                            book.set_availability_status(True)
                            user.remove_borrowed_book(book)

                            input(f"\n'{title}' has been returned, time to read another book! ")
                            return
                        else:
                            input(f"\n'{username}' does not have {book.get_title()} checked out. ")
                            return
                        
                    # If book is not found
                input(f"\nSorry we cannot find '{name}'. Try checking the books you have checked out with the user operations menu. ")
                return

        else:
            input(f"Sorry {username} is not a registered user. ")
            return


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
    
#    <----------> Adding a new user <---------->

    if user_input == '1':

#        ---------- Getting Book Values ----------
        name = input(f"\nWhat is your name? ")
        username = input(f"\nWhat would you like your username to be? ")

#        ---------- Adding the appropriate object to the library ----------
        user_obj = User(name, username)
        library['users'].append(user_obj)

        input(f"\nCongrats {name}, you have been regeistered under the username: {username} ")

#    <----------> View user details <---------->

    if user_input == '2':

#        ---------- Finding the user ----------
        username = input("What is the username of the user you want to view? ")

        for user in library['users']:
            if user.get_username() == username:
                
#                --- Showing the details of the user ---
                print(f'''

{user.get_username()}:

Name: {user.get_name()}
Library ID: {user.get_library_id()}
Borrowed books: ''')

                for book in user.get_borrowed_books():
                    print(book.get_title())
                input("")
                return

            # If the user is not found
        input(f"Sorry, no user exists under the username: '{username}'")

#    <----------> Displaying all users <---------->

    if user_input == '3':
        print('\n')
        for user in library['users']:
            print(f"{user.get_username()}")
        
        input("\n")


        
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
#    <----------> Adding a new author <---------->

    if user_input == '1':

#        ---------- Getting author values ----------
        name = input(f"\nWhat is the authors name? ")
        bio = input(f"\nGive a quick biography for the author: ")

#        ---------- Adding the appropriate object to the library ----------
        author_obj = Author(name, bio)
        library['authors'].append(author_obj)

        input(f"\nThe author {name} has been added to the library! ")

#    <----------> View author details <---------->

    if user_input == '2':

#        ---------- Finding the author ----------
        name = input("What is the name of the author you want to view? ")

        for author in library['authors']:
            if author.get_name() == name:
                
#                --- Showing the details of the author ---
                print(f'''

{author.get_name()}:

{author.get_biography()}

Books written by this author that are in the library:
''')

                for book in author.get_books():
                    print(book.get_title())
                input("")
                return

            # If the user is not found
        input(f"Sorry, no author exists in our library under the name: '{name}'")

#    <----------> Displaying all authors <---------->

    if user_input == '3':
        print('\n')
        for author in library['authors']:
            print(f"{author.get_name()}")
        
        input("\n")


#<====================> Function Calls <====================>

main()