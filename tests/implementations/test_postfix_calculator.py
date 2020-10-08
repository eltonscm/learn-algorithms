import pytest

from implementations.postfix_calculator import postfix_calculator


@pytest.mark.parametrize(
    "expression, expected_result",
    [
        ("1 6 7 * + 1 -", 42),
        ("1 1 + 6 7 * 2 + -", -42),
        ("1", 1),
        ("1 1 +", 2),
        ("10 2 **", 100),
        ("1 2 -", -1),
    ],
)
def test_postfix_calculator(expression, expected_result):
    assert postfix_calculator(expression) == expected_result
