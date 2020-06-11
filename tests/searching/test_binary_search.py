import pytest

from searching.binary_search import binary_search


@pytest.mark.parametrize(
    "arr, item, expected_index",
    (
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([], 1, -1),
    ),
)
def test_binary_search(arr, item, expected_index):
    assert binary_search(arr, item) == expected_index
