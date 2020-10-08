from __future__ import annotations

from typing import Generator, TypeVar

T = TypeVar("T", int, str)


class Node:
    def __init__(self, data: T, previous: Node = None, next_: Node = None) -> None:
        self.data = data
        self.previous = previous
        self.next_ = next_

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return f"Node(data={self.data}, previous={self.previous}, next={self.next_})"

    def __eq__(self, other) -> bool:
        return self.data is other or self.data == other


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        # How to deal with concurrent increment/decrement of this counter?
        self.count: int = 0

    def __len__(self) -> int:
        return self.count

    def __iter__(self) -> Generator[Node]:
        current = self.head
        while current:
            yield current
            current = current.next_

    def __reversed__(self) -> Generator[Node]:
        # Because of the "previous reference" it's possible to reverse an DoublyLinkedList
        current = self.tail
        while current:
            yield current
            current = current.previous

    def __contains__(self, item: T) -> bool:
        # Searching in DoublyLinkedList is `O(n)` on the average and worst case
        for node in self:
            if item == node:
                return True
        return False

    def add_first(self, data: T) -> None:
        # On DoublyLinkedList, `add_first` is a `O(1)` operation
        node = Node(data)
        aux = self.head
        self.head = node
        self.head.next_ = aux
        self.count += 1

        if aux:
            aux.previous = self.head

        if self.count == 1:
            self.tail = self.head

    def add_last(self, data: T) -> None:
        # On DoublyLinkedList, `add_last` is a `O(1)` operation
        node = Node(data)

        if self.count == 0:
            self.head = node
        else:
            self.tail.next_ = node

        node.previous = self.tail
        self.tail = node
        self.count += 1

    def add_before(self, current: Node, data: T) -> None:
        if current == self.head:
            self.add_first(data)
        else:
            old_previous = current.previous
            new_previous = Node(data)

            old_previous.next_ = new_previous
            new_previous.previous = old_previous
            new_previous.next_ = current
            current.previous = new_previous

    def remove_first(self) -> None:
        # On DoublyLinkedList, `remove_first` is a `O(1)` operation
        if self.count != 0:
            self.head = self.head.next_
            self.count -= 1

        if self.head:
            self.head.previous = None
        else:
            self.tail = None

    def remove_last(self) -> None:
        # On DoublyLinkedList, `remove_last` is a `O(1)` operation
        if self.count == 0:
            return

        if self.count == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next_ = None

        self.count -= 1
