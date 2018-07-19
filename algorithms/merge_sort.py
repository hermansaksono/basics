def merge_sort(list_of_numbers):
    """ Return the sorted list using mergesort"""
    # type: (List[int]) -> List[int]
    if len(list_of_numbers) < 2:
        return list_of_numbers
    else:
        middle = int(len(list_of_numbers)/2)
        left_half = list_of_numbers[0:middle]
        right_half = list_of_numbers[middle:]
        accumulator = []
        return __merge(merge_sort(left_half),
                       merge_sort(right_half),
                       accumulator)


def __merge(left, right, accumulator):
    """Merge left, right, and accumulator lists in an ordered way"""
    # type: (List[int], List[int], List[int]) -> List[int]
    if len(left) == 0 and len(right) == 0:
        return accumulator
    elif len(left) == 0:
        return accumulator + right
    elif len(right) == 0:
        return accumulator + left
    elif left[0] < right[0]:
        return __merge(left[1:], right,
                       accumulator + [left[0]])
    elif right[0] < left[0]:
        return __merge(left, right[1:],
                       accumulator + [right[0]])
    else:
        return __merge(left[1:], right,
                       accumulator + [left[0]])