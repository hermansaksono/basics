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
    return memo#[num_eggs][num_floors]


n_eggs = 100
k_floors = 100
#print(get_min_num_trials_memoized(n_eggs, k_floors))

a = get_min_num_trials_memoized(n_eggs, k_floors)
for i in range(1, len(a)):
    print(a[i])

