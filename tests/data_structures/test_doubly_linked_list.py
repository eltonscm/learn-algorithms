import pytest

from data_structures.doubly_linked_list import DoublyLinkedList


@pytest.mark.parametrize("method_name", ("add_first", "add_last"))
def test_add_one_item(method_name):
    linked_list = DoublyLinkedList()
    method = getattr(linked_list, method_name)
    method(1)

    assert len(linked_list) == 1

    head = linked_list.head
    tail = linked_list.tail

    assert head == 1
    assert head.previous is None
    assert head.next_ is None

    assert tail == 1
    assert tail.previous is None
    assert tail.next_ is None


@pytest.mark.parametrize(
    "method_name, expected_head_value, expected_tail_value",
    (("add_first", 2, 1), ("add_last", 1, 2)),
)
def test_add_two_items(method_name, expected_head_value, expected_tail_value):
    linked_list = DoublyLinkedList()
    method = getattr(linked_list, method_name)

    method(1)
    method(2)

    assert len(linked_list) == 2

    head = linked_list.head
    tail = linked_list.tail

    assert head == expected_head_value
    assert head.previous is None
    assert head.next_ == linked_list.tail

    assert tail == expected_tail_value
    assert tail.previous == head
    assert tail.next_ is None


@pytest.mark.parametrize(
    "method_name, expected_head_value, expected_middle_value, expected_tail_value",
    (("add_first", 3, 2, 1), ("add_last", 1, 2, 3)),
)
def test_add_three_items(
    method_name, expected_head_value, expected_middle_value, expected_tail_value,
):
    linked_list = DoublyLinkedList()
    method = getattr(linked_list, method_name)

    method(1)
    method(2)
    method(3)

    assert len(linked_list) == 3

    head = linked_list.head
    middle = head.next_
    tail = linked_list.tail

    assert head == expected_head_value
    assert head.previous is None
    assert head.next_ == middle

    assert middle == expected_middle_value
    assert middle.previous == head
    assert middle.next_ == tail

    assert tail == expected_tail_value
    assert tail.previous == middle
    assert tail.next_ is None


def test_add_before_tail():
    linked_list = DoublyLinkedList()
    linked_list.add_last(1)
    linked_list.add_last(3)

    linked_list.add_before(linked_list.tail, 2)

    head = linked_list.head
    middle = head.next_
    tail = linked_list.tail

    assert head == 1
    assert head.previous is None
    assert head.next_ == middle

    assert middle == 2
    assert middle.previous == head
    assert middle.next_ == tail

    assert tail == 3
    assert tail.previous == middle
    assert tail.next_ is None


def test_add_before_head():
    linked_list = DoublyLinkedList()
    linked_list.add_last(2)
    linked_list.add_last(3)

    linked_list.add_before(linked_list.head, 1)

    head = linked_list.head
    middle = head.next_
    tail = linked_list.tail

    assert head == 1
    assert head.previous is None
    assert head.next_ == middle

    assert middle == 2
    assert middle.previous == head
    assert middle.next_ == tail

    assert tail == 3
    assert tail.previous == middle
    assert tail.next_ is None


@pytest.mark.parametrize(
    "method_name, size, head, tail",
    (
        ("remove_first", 1, None, None),
        ("remove_first", 2, 0, 0),
        ("remove_first", 3, 1, 0),
        ("remove_last", 1, None, None),
        ("remove_last", 2, 1, 1),
        ("remove_last", 3, 2, 1),
    ),
)
def test_remove_added_first(method_name, size, head, tail):
    dll = DoublyLinkedList()

    for n in range(size):
        dll.add_first(n)

    method = getattr(dll, method_name)
    method()

    assert len(dll) == (size - 1)
    assert dll.head == head
    assert dll.tail == tail


@pytest.mark.parametrize(
    "method_name, size, head, tail",
    (
        ("remove_first", 1, None, None),
        ("remove_first", 2, 1, 1),
        ("remove_first", 3, 1, 2),
        ("remove_last", 1, None, None),
        ("remove_last", 2, 0, 0),
        ("remove_last", 3, 0, 1),
    ),
)
def test_remove_added_last(method_name, size, head, tail):
    dll = DoublyLinkedList()

    for n in range(size):
        dll.add_last(n)

    method = getattr(dll, method_name)
    method()

    assert len(dll) == (size - 1)
    assert dll.head == head
    assert dll.tail == tail


def test_iteration():
    linked_list = DoublyLinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)

    values_list = [item for item in linked_list]

    assert values_list == [1, 2, 3]


def test_reversed():
    linked_list = DoublyLinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)

    values_list = [item for item in reversed(linked_list)]

    assert values_list == [3, 2, 1]


def test_container():
    linked_list = DoublyLinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)

    assert 1 in linked_list
    assert 2 in linked_list
    assert 3 not in linked_list
