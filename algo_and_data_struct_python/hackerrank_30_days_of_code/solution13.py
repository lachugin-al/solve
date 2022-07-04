# Абстрактные классы

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass # abstract method


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):      # ovveride abstract method
        print(f'Title: {self.title}\n'
              f'Author: {self.author}\n'
              f'Price: {self.price}')

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
