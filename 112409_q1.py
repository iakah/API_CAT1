class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def mark_as_borrowed(self):
        """Mark the book as borrowed"""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def mark_as_returned(self):
        """Mark the book as returned"""
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Borrow a book if it's available"""
        if not book.is_borrowed:
            if book.mark_as_borrowed():
                self.borrowed_books.append(book)
                print(f"{self.name} successfully borrowed '{book.title}'")
                return True
        else:
            print(f"Sorry, '{book.title}' is already borrowed")
        return False
    
    def return_book(self, book):
        """Return a borrowed book"""
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"{self.name} successfully returned '{book.title}'")
                return True
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'")
        return False
    
    def list_borrowed_books(self):
        """List all books borrowed by this member"""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books")
        else:
            print(f"\n{self.name}'s borrowed books:")
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book.title} by {book.author}")
    
    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


# Library Management System
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def display_books(self):
        print("\nLibrary Books")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
    
    def display_members(self):
        print("\nLibrary Members")
        for i, member in enumerate(self.members, 1):
            print(f"{i}. {member}")


def main():
    # Initialize library
    library = Library()
    
    # Add sample books
    books = [
        Book("Weep Not, Child", "Ngugi wa Thiong'o"),
        Book("The River and the Source", "Margaret Ogola"),
        Book("Petals of Blood", "Ngugi wa Thiong'o"),
        Book("I Will Marry When I Want", "Ngugi wa Thiong'o"),
        Book("The Beautiful Ones Are Not Yet Born", "Ayi Kwei Armah")
    ]
    
    for book in books:
        library.add_book(book)
    
    # Add sample members
    members = [
        LibraryMember("Wanjiku Muthoni", "M001"),
        LibraryMember("Kiprop Chelimo", "M002"),
        LibraryMember("Amina Hassan", "M003")
    ]
    
    for member in members:
        library.add_member(member)
    
    print("Welcome to the Library Management System")
    
    while True:
        print("\nMain Menu")
        print("1. Display all books")
        print("2. Display all members")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List member's borrowed books")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            library.display_books()
        
        elif choice == '2':
            library.display_members()
        
        elif choice == '3':
            # Borrow a book
            library.display_members()
            try:
                member_idx = int(input("\nSelect member (enter number): ")) - 1
                if 0 <= member_idx < len(library.members):
                    selected_member = library.members[member_idx]
                    
                    # Show available books only
                    available_books = [book for book in library.books if not book.is_borrowed]
                    if not available_books:
                        print("No books available for borrowing")
                        continue
                    
                    print("\nAvailable Books")
                    for i, book in enumerate(available_books, 1):
                        print(f"{i}. {book}")
                    
                    book_idx = int(input("\nSelect book to borrow (enter number): ")) - 1
                    if 0 <= book_idx < len(available_books):
                        selected_book = available_books[book_idx]
                        selected_member.borrow_book(selected_book)
                    else:
                        print("Invalid book selection")
                else:
                    print("Invalid member selection")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '4':
            # Return a book
            library.display_members()
            try:
                member_idx = int(input("\nSelect member (enter number): ")) - 1
                if 0 <= member_idx < len(library.members):
                    selected_member = library.members[member_idx]
                    
                    if not selected_member.borrowed_books:
                        print(f"{selected_member.name} has no books to return")
                        continue
                    
                    print(f"\n{selected_member.name}'s Borrowed Books")
                    for i, book in enumerate(selected_member.borrowed_books, 1):
                        print(f"{i}. {book}")
                    
                    book_idx = int(input("\nSelect book to return (enter number): ")) - 1
                    if 0 <= book_idx < len(selected_member.borrowed_books):
                        selected_book = selected_member.borrowed_books[book_idx]
                        selected_member.return_book(selected_book)
                    else:
                        print("Invalid book selection")
                else:
                    print("Invalid member selection")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '5':
            # List borrowed books
            library.display_members()
            try:
                member_idx = int(input("\nSelect member (enter number): ")) - 1
                if 0 <= member_idx < len(library.members):
                    selected_member = library.members[member_idx]
                    selected_member.list_borrowed_books()
                else:
                    print("Invalid member selection")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '6':
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()