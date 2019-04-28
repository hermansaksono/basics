def get_min_num_trials_memoized(num_eggs, num_floors):
    memo = [[0] * (num_floors + 1) for i in range(num_eggs + 1)]
    for egg in range(1, num_eggs + 1):
        for floor in range(1, num_floors + 1):
            if floor == 1:
                memo[egg][1] = 1
            elif egg == 1:
                memo[1][floor] = floor
            else:
                memo[egg][floor] = num_floors
                for i in range(1, floor):
                    egg_break = memo[egg - 1][i - 1]
                    egg_doesnt_break = memo[egg][floor - i]
                    num_trials = 1 + max(egg_break, egg_doesnt_break)
                    memo[egg][floor] = min(num_trials, memo[egg][floor])
    return memo


def get_path(memo, num_floors, path):
    if len(memo) is 1:
        return path
    else:
        max_trials = memo[-1][num_floors]
        optimal_num_eggs_index = get_optimal_egg_index(memo)
        next_floor_index = get_next_floor_index(memo[optimal_num_eggs_index], num_floors, max_trials)
        next_path = get_next_floors(path, next_floor_index)
        return get_path(memo[:optimal_num_eggs_index], next_floor_index, next_path)


def get_next_floor_index(floor_memo, last_floor_index, max_trials):
    if floor_memo[last_floor_index] == 0:
        return 1
    elif floor_memo[last_floor_index] < max_trials:
        return last_floor_index
    else:
        return get_next_floor_index(floor_memo, last_floor_index - 1, max_trials)


def get_next_floors(path, floor_index):
    if floor_index is 1:
        return path + range(path[-1]-1, 0, -1)
    else:
        return path + [floor_index + 1]


def get_optimal_egg_index(memo):
    if len(memo) <= 2:
        return 1
    elif memo[-1][-1] < memo[-2][-1]:
        return len(memo) - 1
    else:
        return get_optimal_egg_index(memo[:-1])

n_eggs = 5
k_floors = 20
#print(get_min_num_trials_memoized(n_eggs, k_floors))

egg_drop_memo = get_min_num_trials_memoized(n_eggs, k_floors)
for i in range(0, len(egg_drop_memo)):
    print(egg_drop_memo[i])
    pass

print(get_path(egg_drop_memo, k_floors, []))

