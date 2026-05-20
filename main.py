from library_system import LibrarySystem
from exceptions import LibraryError


def menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Add Member")
    print("4. Display Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Loans")
    print("8. Exit")


library = LibrarySystem()

while True:
    menu()
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            member_id = input("Member ID: ")
            name = input("Member Name: ")
            library.add_member(member_id, name)

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == "6":
            member_id = input("Member ID: ")
            book_id = input("Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == "7":
            library.display_loans()

        elif choice == "8":
            print("Exiting Library System...")
            break

        else:
            print("Invalid choice. Try again.")

    except LibraryError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")