# TODO:
# 1) Define class Book with attributes: title, author, price
# 2) Implement method get_details(self) -> "Title: <...>, Author: <...>, Price: <...>"
# 3) Create 3 Book instances and print their details using get_details()

class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 9.99)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 7.99)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)

    print(book1.get_details())
    print(book2.get_details())
    print(book3.get_details())
