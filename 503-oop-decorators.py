from dataclasses import dataclass
from typing import List


class Book:

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.isbn == other.isbn and self.title == other.title and self.author == other.author

    def __str__(self):
        return f'isbn: {self.isbn}...'


@dataclass
class Book2:
    isbn: str
    title: str
    author: str


@dataclass
class Product:
    name: str
    value: float

    def __gt__(self, other):
        return self.value > other.value


@dataclass
class Basket:
    products: List[Product]

    def __contains__(self, item):
        return item in self.products


if __name__ == '__main__':
    pt1 = Book2('abc', 'Pan Tadeusz', 'Adam Mickiewicz')
    pt2 = Book('abc', 'Pan Tadeusz', 'Adam Mickiewicz')

    print(pt1 == pt2)
    print(pt1)
    print(pt2)

    coke = Product('coca cola', 2.0)
    pepsi = Product('pepsi', 2.5)

    print(pepsi > coke)

    basket = Basket([coke, pepsi])
    print(coke in basket)
