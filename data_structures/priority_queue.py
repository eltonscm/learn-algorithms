from __future__ import annotations

from typing import Generator

from data_structures.doubly_linked_list import DoublyLinkedList, T


class PriorityQueue:
    def __init__(self):
        self._list = DoublyLinkedList()

    def __len__(self) -> int:
        return len(self._list)

    def __iter__(self) -> Generator[T]:
        yield from self._list

    def enqueue(self, data: T) -> None:
        if len(self) == 0:
            self._list.add_last(data)
        else:
            current = self._list.head

            while current and current.data > data:
                current = current.next_

            if current is None:
                self._list.add_last(data)
            else:
                self._list.add_before(current, data)

    def peek(self) -> T:
        if len(self) == 0:
            raise IndexError("peek from empty priority queue")
        return self._list.head.data

    def dequeue(self) -> T:
        if len(self) == 0:
            raise IndexError("dequeue from empty priority queue")
        data = self.peek()
        self._list.remove_first()
        return data
