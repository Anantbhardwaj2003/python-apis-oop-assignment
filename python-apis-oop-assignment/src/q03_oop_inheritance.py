# TODO:
# Create subclass EBook(Book) with extra attribute file_size (MB: float|int)
# Override get_details to include file_size, e.g., "... , File Size: 2.5MB"
# Instantiate EBook and print details + discounted price.

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

class EBook(Book):
    def __init__(self, title: str, author: str, price: float, file_size: float):
        super().__init__(title, author, price)
        self.file_size = file_size

    def get_details(self) -> str:
        return f"{super().get_details()}, File Size: {self.file_size}MB"

if __name__ == "__main__":
    ebook = EBook("Digital Fortress", "Dan Brown", 14.99, 2.5)
    print(ebook.get_details())
    print("Price after discount:", ebook.get_price_after_discount())
    ebook.discount = 0.15
    print("Updated", ebook.get_details())
    print("Price after discount:", ebook.get_price_after_discount())
