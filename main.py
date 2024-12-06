class Book:
    def __init__(self, title, author, isbn, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre

    # Getters and setters for encapsulation
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def display_book_info(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}"

# Class for Fiction books, inheriting from Book
class FictionBook(Book):
    def __init__(self, title, author, isbn, genre, sub_genre):
        super().__init__(title, author, isbn, genre)
        self.__sub_genre = sub_genre

    def get_sub_genre(self):
        return self.__sub_genre

    def set_sub_genre(self, sub_genre):
        self.__sub_genre = sub_genre

    def display_book_info(self):
        return super().display_book_info() + f", Sub-genre: {self.__sub_genre}"

# Class for Non-Fiction books, inheriting from Book
class NonFictionBook(Book):
    def __init__(self, title, author, isbn, genre, field_of_study):
        super().__init__(title, author, isbn, genre)
        self.__field_of_study = field_of_study

    def get_field_of_study(self):
        return self.__field_of_study

    def set_field_of_study(self, field_of_study):
        self.__field_of_study = field_of_study

    def display_book_info(self):
        return super().display_book_info() + f", Field of Study: {self.__field_of_study}"

class Member:
    def __init__(self, member_id, name, email):
        self.__member_id = member_id
        self.__name = name
        self.__email = email

    # Getters and setters for encapsulation
    def get_member_id(self):
        return self.__member_id

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def display_member_info(self):
        return f"Member ID: {self.__member_id}, Name: {self.__name}, Email: {self.__email}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = {}

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                self.books.remove(book)
                return f"Book with ISBN {isbn} removed."
        return "Book not found."

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.get_member_id() == member_id:
                self.members.remove(member)
                return f"Member with ID {member_id} removed."
        return "Member not found."

    def borrow_book(self, member_id, isbn):
        if member_id not in self.borrowed_books:
            self.borrowed_books[member_id] = []
        for book in self.books:
            if book.get_isbn() == isbn:
                self.borrowed_books[member_id].append(book)
                return f"Book '{book.get_title()}' borrowed by member ID {member_id}."
        return "Book not found."

    def return_book(self, member_id, isbn):
        if member_id in self.borrowed_books:
            for book in self.borrowed_books[member_id]:
                if book.get_isbn() == isbn:
                    self.borrowed_books[member_id].remove(book)
                    return f"Book '{book.get_title()}' returned."
        return "Book not found in borrowed list."

    def display_books(self):
        for book in self.books:
            print(book.display_book_info())

    def display_members(self):
        for member in self.members:
            print(member.display_member_info())

# Example usage:
library = Library()

# Adding books
book1 = FictionBook("The Hobbit", "J.R.R. Tolkien", "1234567890", "Fantasy", "Epic")
book2 = NonFictionBook("A Brief History of Time", "Stephen Hawking", "0987654321", "Science", "Physics")
library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member(1, "Alice", "alice@example.com")
member2 = Member(2, "Bob", "bob@example.com")
library.add_member(member1)
library.add_member(member2)

# Borrowing a book
print(library.borrow_book(1, "1234567890"))

# Returning a book
print(library.return_book(1, "1234567890"))

# Display books and members
print("\nBooks in Library:")
library.display_books()

print("\nMembers in Library:")
library.display_members()

# Removing a book
print(library.remove_book("1234567890"))
