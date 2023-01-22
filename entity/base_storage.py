from typing import Dict

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughtProduct, NotEnoughtSpace


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        """
        Проверка, что достаточно места
        и добавление товара
        """
        if self.get_free_space() < amount:
            raise NotEnoughtSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        """
        Проверка, есть ли такой товар.
        Вычитание необходимого количества товара.
        Если товара станет 0 - удаление товара из списка.
        """
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughtProduct

        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self) -> int:
        """
        Подсчёт суммы значений в словаре __items.
        Вычитание её из __capacity
        """
        return self.__capacity - sum(self.__items.values())

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, new_data):
        self.__items = new_data

    def get_unique_items_count(self):
        return len(self.__items)
