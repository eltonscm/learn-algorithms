import pytest

from data_structures.priority_queue import PriorityQueue


@pytest.mark.parametrize(
    "items, expected_head", [([1], 1), ([1, 2], 2), ([2, 1], 2), ([2, 1, 3], 3)]
)
def test_enqueue(items, expected_head):
    queue = PriorityQueue()
    for item in items:
        queue.enqueue(item)

    assert len(queue) == len(items)
    assert queue.peek() == expected_head


def test_peek():
    queue = PriorityQueue()
    queue.enqueue("a")
    queue.enqueue("b")

    assert queue.peek() == "b"
    assert len(queue) == 2


def test_peek_empty_queue():
    queue = PriorityQueue()

    with pytest.raises(IndexError) as exc:
        queue.peek()

    assert str(exc.value) == "peek from empty priority queue"


def test_dequeue():
    queue = PriorityQueue()
    queue.enqueue("a")
    queue.enqueue("b")

    assert queue.dequeue() == "b"
    assert len(queue) == 1


def test_dequeue_empty_queue():
    queue = PriorityQueue()

    with pytest.raises(IndexError) as exc:
        queue.dequeue()

    assert str(exc.value) == "dequeue from empty priority queue"


def test_iter():
    queue = PriorityQueue()
    queue.enqueue("a")
    queue.enqueue("c")
    queue.enqueue("b")

    assert [item for item in queue] == ["c", "b", "a"]
