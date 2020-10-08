from __future__ import annotations

from typing import Generator

from data_structures.linked_list import LinkedList, T


class Queue:
    def __init__(self):
        self._list = LinkedList()

    def __len__(self) -> int:
        return len(self._list)

    def __iter__(self) -> Generator[T]:
        yield from self._list

    def enqueue(self, data: T) -> None:
        self._list.add_last(data)

    def peek(self) -> T:
        if len(self) == 0:
            raise IndexError("peek from empty queue")
        return self._list.head.data

    def dequeue(self) -> T:
        if len(self) == 0:
            raise IndexError("dequeue from empty queue")
        data = self.peek()
        self._list.remove_first()
        return data
