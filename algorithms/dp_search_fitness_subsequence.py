import sys
from fitness_intensities import list_of_fitness_intensities

sys.setrecursionlimit(1500)


def get_memoized_bouts(list_of_intensities, minimum_intensity, max_length):
    length = len(list_of_intensities)
    memo = [[0] * max_length for i in range(length)]
    for minute_index in range(0, length):
        for duration_index in range(0, max_length):
            if duration_index is 0:
                memo[minute_index][duration_index] = is_minimum_active(list_of_intensities[minute_index],
                                                                       minimum_intensity)
            else:
                memo[minute_index][duration_index] = is_minimum_active(list_of_intensities[minute_index],
                                                                       minimum_intensity) \
                                                     + memo[minute_index - 1][duration_index - 1]
    return memo


def get_bout_points(memoized_bouts, min_bout_length, tolerance, max_length):
    return get_bout_points_recursion(memoized_bouts, min_bout_length, tolerance, max_length, [])


def get_bout_points_recursion(memoized_bouts, min_bout_length, tolerance, max_length, list_of_bouts):
    tolerated_bout_length = min_bout_length + tolerance - 1
    end_minute = len(memoized_bouts) - 1
    if end_minute < 0:
        return list_of_bouts
    elif memoized_bouts[end_minute][tolerated_bout_length] < min_bout_length:
        return get_bout_points_recursion(memoized_bouts[:end_minute],
                                         min_bout_length,
                                         tolerance,
                                         max_length,
                                         list_of_bouts)
    else:
        bout_length = get_maximum_bout_length(memoized_bouts, end_minute, tolerated_bout_length, max_length)
        return get_bout_points_recursion(memoized_bouts[:end_minute - bout_length],
                                         min_bout_length,
                                         tolerance,
                                         max_length,
                                         [(end_minute - bout_length, end_minute)] + list_of_bouts)


def is_minimum_active(intensity, minimum):
    return 1 if intensity >= minimum else 0


def get_maximum_bout_length(memoized_bouts, end_minute, bout_length_index, max_length):
    if bout_length_index > len(memoized_bouts):
        return 0
    elif bout_length_index > max_length:
        return max_length - 1
    elif memoized_bouts[end_minute][bout_length_index] >= memoized_bouts[end_minute][bout_length_index + 1]:
        return bout_length_index
    else:
        return get_maximum_bout_length(memoized_bouts, end_minute, bout_length_index + 1, max_length)


subset = list_of_fitness_intensities

all_bouts = get_memoized_bouts(subset, 2, 120)
for i in range(0, 40):
    print(str(i) + ": " + str(all_bouts[i]))
    pass

active_bouts = get_bout_points(all_bouts, 5, 1, 120)
print("Active bouts: " + str(active_bouts))
