from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotAvailableError,
    MemberLimitError,
    BookNotFoundError,
    MemberNotFoundError,
)


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    # ---------------- BOOK METHODS ----------------
    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- Book List ---")
        for book in self.books:
            print(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        raise BookNotFoundError("Book not found.")

    # ---------------- MEMBER METHODS ----------------
    def add_member(self, member_id, name):
        member = Member(member_id, name)
        self.members.append(member)
        print("Member added successfully!")

    def display_members(self):
        if not self.members:
            print("No members found.")
            return

        print("\n--- Member List ---")
        for member in self.members:
            print(member)

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        raise MemberNotFoundError("Member not found.")

    # ---------------- BORROW METHODS ----------------
    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not book.available:
            raise BookNotAvailableError("Book is already borrowed.")

        if not member.borrow_book(book):
            raise MemberLimitError("Member reached maximum loan limit.")

        book.borrow_book()
        loan = Loan(book, member)
        self.loans.append(loan)

        print(f"{member.name} borrowed '{book.title}' successfully.")

    # ---------------- RETURN METHODS ----------------
    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        member.return_book(book)
        book.return_book()

        print(f"{member.name} returned '{book.title}' successfully.")

    # ---------------- LOAN DISPLAY ----------------
    def display_loans(self):
        if not self.loans:
            print("No active loans.")
            return

        print("\n--- Loan Records ---")
        for loan in self.loans:
            print(loan)