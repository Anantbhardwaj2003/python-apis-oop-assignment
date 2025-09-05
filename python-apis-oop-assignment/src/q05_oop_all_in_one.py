# TODO (combined OOP exercise):
# Build a small library domain:
# 1) Class Price(value: float, currency: str="INR")
#    - __post_init__ style validation in __init__
#    - __repr__/__str__ to show "INR 499.00"
# 2) Class Book(title, author, price: Price)
#    - __eq__ compares title+author
#    - classmethod from_dict(d: dict) -> Book
# 3) Class Inventory:
#    - holds books (composition) in a list
#    - add_book(book), remove_book(title, author)
#    - find_by_author(author) -> list[Book]
#    - __len__ returns count, __iter__ yields books
# Demo:
# - Create 3 books via from_dict, add to inventory, print all (uses __str__)
# - Remove one, print length, print books by a specific author.

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        self.value = value
        self.currency = currency

    def __repr__(self):
        return f"{self.currency} {self.value:.2f}"

class Book:
    def __init__(self, title: str, author: str, price: Price):
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    @classmethod
    def from_dict(cls, d: dict) -> "Book":
        title = d.get("title", "")
        author = d.get("author", "")
        price = Price(**d.get("price", {}))
        return cls(title, author, price)

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str, author: str):
        self.books = [book for book in self.books if book.title != title or book.author != author]

    def find_by_author(self, author: str) -> list[Book]:
        return [book for book in self.books if book.author == author]

    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return iter(self.books)

if __name__ == "__main__":
    book_dicts = [
        {"title": "1984", "author": "George Orwell", "price": {"value": 9.99, "currency": "USD"}},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": {"value": 7.99, "currency": "USD"}},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": {"value": 10.99, "currency": "USD"}},
    ]

    inventory = Inventory()

    for bd in book_dicts:
        book = Book.from_dict(bd)
        inventory.add_book(book)

    print("All books in inventory:")
    for book in inventory:
        print(f"{book.title} by {book.author}, Price: {book.price}")

    inventory.remove_book("1984", "George Orwell")
    print(f"\nInventory length after removal: {len(inventory)}")

    author_to_find = "Harper Lee"
    print(f"\nBooks by {author_to_find}:")
    for book in inventory.find_by_author(author_to_find):
        print(f"{book.title} by {book.author}, Price: {book.price}")
