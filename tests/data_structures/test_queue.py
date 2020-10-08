import pytest

from data_structures.queue import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)

    assert len(queue) == 1


def test_peek():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("n")

    assert queue.peek() == "a"
    assert len(queue) == 2


def test_peek_empty_queue():
    queue = Queue()

    with pytest.raises(IndexError) as exc:
        queue.peek()

    assert str(exc.value) == "peek from empty queue"


def test_dequeue():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")

    assert queue.dequeue() == "a"
    assert len(queue) == 1


def test_dequeue_empty_queue():
    queue = Queue()

    with pytest.raises(IndexError) as exc:
        queue.dequeue()

    assert str(exc.value) == "dequeue from empty queue"


def test_iter():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")

    assert [item for item in queue] == ["a", "b", "c"]
