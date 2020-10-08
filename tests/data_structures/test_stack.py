import pytest

from data_structures.stack import Stack


def test_push():
    stack = Stack()
    stack.push(1)

    assert len(stack) == 1


def test_peek():
    stack = Stack()
    stack.push("a")
    stack.push("b")

    assert stack.peek() == "b"
    assert len(stack) == 2


def test_peek_empty_stack():
    stack = Stack()

    with pytest.raises(IndexError) as exc:
        stack.peek()

    assert str(exc.value) == "peek from empty list"


def test_pop():
    stack = Stack()
    stack.push("a")
    stack.push("b")

    assert stack.pop() == "b"
    assert len(stack) == 1


def test_pop_empty_stack():
    stack = Stack()

    with pytest.raises(IndexError) as exc:
        stack.pop()

    assert str(exc.value) == "pop from empty list"


def test_iter():
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")

    assert [item for item in stack] == ["c", "b", "a"]
