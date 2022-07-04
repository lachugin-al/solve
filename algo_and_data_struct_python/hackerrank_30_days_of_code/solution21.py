# Дженерики / Generics

from typing import TypeVar

Element = TypeVar("Element")


def printArray(array: [Element]): # принимает на вход массив
    for element in array:
        print(element)


vInt = [1, 2, 3]
vString = ["Hello", "World"]

printArray(vInt)
printArray(vString)