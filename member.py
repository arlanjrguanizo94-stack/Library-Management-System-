class Member:
    MAX_LOANS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_LOANS:
            return False

        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"[{self.member_id}] {self.name} - Borrowed Books: {len(self.borrowed_books)}"