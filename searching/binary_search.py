def binary_search(arr, item):
    """Does a search for the index of a `item` on a sorted sequence using
    the "divide & conquer" strategy.

    Args:
        arr (Sequence[int]): a sorted sequence of integers
        item (int): the item that will be searched on `arr`

    Returns:
        int: index of found item or `-1` if not found
    """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return -1
