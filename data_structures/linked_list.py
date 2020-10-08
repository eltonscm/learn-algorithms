from __future__ import annotations

from typing import Generator, TypeVar

T = TypeVar("T", int, str)


class Node:
    def __init__(self, data: T, next_: Node = None) -> None:
        self.data = data
        self.next_ = next_

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"Node(data={self.data}, next={self.next_})"

    def __eq__(self, other) -> bool:
        return self.data is other or self.data == other


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        # How to deal with concurrent increment/decrement of this counter?
        self.count: int = 0

    def __len__(self) -> int:
        return self.count

    def __iter__(self) -> Generator[T]:
        current = self.head
        while current:
            yield current.data
            current = current.next_

    def __contains__(self, item: T) -> bool:
        # Searching in LinkedList is `O(n)` on the average and worst case
        for node in self:
            if item == node:
                return True
        return False

    def add_first(self, data: T) -> None:
        # On LinkedList, `add_first` is a `O(1)` operation
        node = Node(data)
        aux = self.head
        self.head = node
        self.head.next_ = aux
        self.count += 1

        if self.count == 1:
            self.tail = self.head

    def add_last(self, data: T) -> None:
        # On LinkedList, `add_last` is a `O(1)` operation
        node = Node(data)

        if self.count == 0:
            self.head = node
        else:
            self.tail.next_ = node

        self.tail = node
        self.count += 1

    def remove_first(self) -> None:
        # On LinkedList, `remove_first` is a `O(1)` operation
        if self.count != 0:
            aux = self.head
            self.head = aux.next_
            self.count -= 1

        if self.count == 0:
            self.tail = None

    def remove_last(self) -> None:
        # On LinkedList, `remove_last` is a `O(n)` operation
        if self.count <= 1:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next_ != self.tail:
                current = current.next_
            current.next_ = None
            self.tail = current
        self.count -= 1
