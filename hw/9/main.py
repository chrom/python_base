# 1. Описать класс, реализующий десятичный счетчик, который может увеличивать или
# уменьшать свое значение на единицу в заданном диапазоне. Предусмотреть инициализацию
# счетчика значениями по умолчанию и произвольными значениями. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояни


class Counter:
    def __init__(self, counter: int = 0):
        self.__counter = counter

    def increase(self):
        self.__counter += 1

    def decrease(self):
        self.__counter -= 1

    def counter(self):
        return self.__counter


c = Counter(10)
c.increase()
c.increase()
print(c.counter())
c.__counter = 20
print(c.__counter)
print(dir(c))
print(c._Counter__counter)
c.decrease()
c.decrease()
print(c.__counter)

# 2. Описать класс «домашняя библиотека». Предусмотреть возможность работы с произвольным числом книг,
# поиска книги по какому-либо признаку (например, по автору или по году издания), добавления книг в библиотеку,
# удаления книг из нее, сортировки книг по разным полям.
import collections


# class Library(collections.UserDict(init)):

