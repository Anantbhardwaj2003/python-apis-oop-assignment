# TODO:
# Extend Book with a "private" discount attribute _discount (default=0.1)
# Add getter/setter for discount with validation (0.0 <= discount <= 0.9)
# Add method get_price_after_discount() -> price*(1-discount)
# Demonstrate setting discount via setter and print the discounted price.

class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def get_details(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Discount: {self._discount}"

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float):
        if 0.0 <= value <= 0.9:
            self._discount = value
        else:
            raise ValueError("Discount must be between 0.0 and 0.9")

    def get_price_after_discount(self) -> float:
        return self.price * (1 - self._discount)

if __name__ == "__main__":
    book = Book("1984", "George Orwell", 9.99)
    print(book.get_details())
    print("Price after discount:", book.get_price_after_discount())
    book.discount = 0.2
    print("Updated", book.get_details())
    print("Price after discount:", book.get_price_after_discount())
