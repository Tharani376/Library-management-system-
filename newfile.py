class Library:
    def __init__(self):
        self.books = {}
        self.lent_books = {}

    def add_book(self, book_name):
        if book_name in self.books:
            print(f"'{book_name}' is already in the library.")
        else:
            self.books[book_name] = True
            print(f"'{book_name}' has been added to the library.")

    def display_books(self):
        print("\nBooks available in the library:")
        for book, available in self.books.items():
            status = "Available" if available else f"Lent to {self.lent_books.get(book)}"
            print(f"- {book} ({status})")

    def lend_book(self, book_name, user):
        if book_name in self.books:
            if self.books[book_name]:
                self.books[book_name] = False
                self.lent_books[book_name] = user
                print(f"'{book_name}' has been lent to {user}.")
            else:
                print(f"Sorry, '{book_name}' is currently lent to {self.lent_books[book_name]}.")
        else:
            print(f"'{book_name}' is not in the library.")

    def return_book(self, book_name):
        if book_name in self.lent_books:
            self.books[book_name] = True
            user = self.lent_books.pop(book_name)
            print(f"'{book_name}' returned by {user}.")
        else:
            print(f"'{book_name}' was not lent out.")

def main():
    library = Library()

    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book = input("Enter book name to add: ")
            library.add_book(book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book = input("Enter book name to lend: ")
            user = input("Enter your name: ")
            library.lend_book(book, user)

        elif choice == '4':
            book = input("Enter book name to return: ")
            library.return_book(book)

        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")




