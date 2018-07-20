def quick_sort(list_of_numbers):
    """Return sorted list using quicksort"""
    # type: (list[int]) -> list[int]
    if len(list_of_numbers) == 0:
        return []
    else:
        pivot = list_of_numbers[0]
        smallers = get_smallers(list_of_numbers, pivot)
        largers = get_largers(list_of_numbers, pivot)

        return quick_sort(smallers) + [pivot] + quick_sort(largers)


def get_smallers(list_of_numbers, pivot):
    """Return list of numbers smaller than pivot"""
    # type: (list[int], int) -> list[int]
    if len(list_of_numbers) == 0:
        return []
    else:
        if list_of_numbers[0] < pivot:
            return [list_of_numbers[0]] + get_smallers(list_of_numbers[1:], pivot)
        else:
            return get_smallers(list_of_numbers[1:], pivot)


def get_largers(list_of_numbers, pivot):
    """Return list of numbers larger than pivot"""
    # type: (list[int], int) -> list[int]
    if len(list_of_numbers) == 0:
        return []
    else:
        if list_of_numbers[0] >= pivot:
            return [list_of_numbers[0]] + get_largers(list_of_numbers[1:], pivot)
        else:
            return get_largers(list_of_numbers[1:], pivot)
