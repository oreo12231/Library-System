# ── Book Class ─────────────────────────────────────────────────
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Starts as not borrowed

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' wasn't borrowed, so it cannot be returned.")
        else:
            self.is_borrowed = False
            print(f"'{self.title}' has been returned.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} [{status}]"


# ── Library ────────────────────────────────────────────────────
# Create 3 Book objects
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("The Hobbit", "J.R.R. Tolkien")

print("=" * 42)
print(" Library System")
print("=" * 42)

# Print each book (uses __str__ automatically)
print("\n--- Initial Catalog ---")
print(book1)
print(book2)
print(book3)

# Borrow some books
print("\n--- Borrowing Books ---")
book1.borrow()
book2.borrow()

# Try to borrow the same book twice (tests the guard message)
book1.borrow()

# Return a book
print("\n--- Returning Books ---")
book1.return_book()

# Try to return a book that was never borrowed (tests the guard message)
book3.return_book()

# Print each book again to show updated status
print("\n--- Updated Catalog ---")
print(book1)
print(book2)
print(book3)
