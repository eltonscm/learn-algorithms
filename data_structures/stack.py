from __future__ import annotations

from typing import Generator

from data_structures.linked_list import LinkedList, T


class Stack:
    def __init__(self) -> None:
        self._list = LinkedList()

    def __len__(self) -> int:
        return len(self._list)

    def __iter__(self) -> Generator[T]:
        for item in self._list:
            yield item

    def push(self, data: T) -> None:
        self._list.add_first(data)

    def peek(self) -> T:
        if len(self._list) == 0:
            raise IndexError("peek from empty list")
        return self._list.head.data

    def pop(self) -> T:
        if len(self._list) == 0:
            raise IndexError("pop from empty list")
        data = self._list.head.data
        self._list.remove_first()
        return data
