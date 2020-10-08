# from data_structures.linked_list import LinkedList, Node
from data_structures.linked_list import LinkedList


def test_add_first_one_item():
    linked_list = LinkedList()
    linked_list.add_first(1)

    assert len(linked_list) == 1
    assert linked_list.head == 1
    assert linked_list.tail == 1


def test_add_first_two_items():
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)

    assert len(linked_list) == 2
    assert linked_list.head == 2
    assert linked_list.tail == 1
    assert linked_list.tail.next_ is None


def test_add_first_three_items():
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.add_first(3)

    assert len(linked_list) == 3
    assert linked_list.head == 3
    assert linked_list.head.next_ == 2
    assert linked_list.tail == 1
    assert linked_list.tail.next_ is None


def test_add_last_one_item():
    linked_list = LinkedList()
    linked_list.add_last(1)

    assert len(linked_list) == 1
    assert linked_list.head == 1
    assert linked_list.tail == 1


def test_add_last_two_items():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)

    assert len(linked_list) == 2
    assert linked_list.head == 1
    assert linked_list.tail == 2
    assert linked_list.tail.next_ is None


def test_add_last_three_items():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)

    assert len(linked_list) == 3
    assert linked_list.head == 1
    assert linked_list.head.next_ == 2
    assert linked_list.tail == 3
    assert linked_list.tail.next_ is None


def test_remove_first_with_one_item():
    linked_list = LinkedList()
    linked_list.add_last(1)

    linked_list.remove_first()

    assert len(linked_list) == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_remove_first_with_two_items():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)

    linked_list.remove_first()

    assert len(linked_list) == 1
    assert linked_list.head == 2
    assert linked_list.tail == 2


def test_remove_first_with_three_items():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)

    linked_list.remove_first()

    assert len(linked_list) == 2
    assert linked_list.head == 2
    assert linked_list.tail == 3


def test_remove_last_with_one_item():
    linked_list = LinkedList()
    linked_list.add_first(1)

    linked_list.remove_last()

    assert len(linked_list) == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_remove_last_with_two_items():
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)

    linked_list.remove_last()

    assert len(linked_list) == 1
    assert linked_list.head == 2
    assert linked_list.tail == 2


def test_remove_last_with_three_items():
    linked_list = LinkedList()
    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.add_first(3)

    linked_list.remove_last()

    assert len(linked_list) == 2
    assert linked_list.head == 3
    assert linked_list.tail == 2


def test_iteration():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)
    linked_list.add_last(3)

    values_list = [item for item in linked_list]

    assert values_list == [1, 2, 3]


def test_container():
    linked_list = LinkedList()
    linked_list.add_last(1)
    linked_list.add_last(2)

    assert 1 in linked_list
    assert 2 in linked_list
    assert 3 not in linked_list
