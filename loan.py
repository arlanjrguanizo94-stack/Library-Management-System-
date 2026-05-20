from datetime import datetime


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.loan_date = datetime.now()

    def __str__(self):
        return (
            f"Book: {self.book.title} | "
            f"Member: {self.member.name} | "
            f"Date Borrowed: {self.loan_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )