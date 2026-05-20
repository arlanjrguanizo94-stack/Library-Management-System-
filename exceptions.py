class LibraryError(Exception):
    """Base exception class for the library system."""
    pass


class BookNotAvailableError(LibraryError):
    """Raised when a book is not available for loan."""
    pass


class MemberLimitError(LibraryError):
    """Raised when a member reaches the loan limit."""
    pass


class BookNotFoundError(LibraryError):
    """Raised when a book cannot be found."""
    pass


class MemberNotFoundError(LibraryError):
    """Raised when a member cannot be found."""
    pass